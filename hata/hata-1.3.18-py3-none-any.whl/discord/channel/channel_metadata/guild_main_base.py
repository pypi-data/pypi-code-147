__all__ = ('ChannelMetadataGuildMainBase',)

from scarletio import copy_docs

from ...core import GUILDS
from ...permission import Permission
from ...permission.permission import (
    PERMISSION_ALL, PERMISSION_MASK_ADMINISTRATOR, PERMISSION_MASK_VIEW_CHANNEL, PERMISSION_NONE
)
from ...user import ClientUserBase

from .fields import (
    parse_permission_overwrites, parse_position, put_permission_overwrites_into, put_position_into,
    validate_permission_overwrites, validate_position
)

from .guild_base import ChannelMetadataGuildBase


class ChannelMetadataGuildMainBase(ChannelMetadataGuildBase):
    """
    Base class for main guild metadata channels not including thread channels.
    
    Attributes
    ----------
    _permission_cache : `None`, `dict` of (`int`, ``Permission``) items
        A `user_id` to ``Permission`` relation mapping for caching permissions. Defaults to `None`.
    parent_id : `int`
        The channel's parent's identifier.
    name : `str`
        The channel's name.
    permission_overwrites : `dict` of (`int`, ``PermissionOverwrite``) items
        The channel's permission overwrites.
    position : `int`
        The channel's position.
    
    Class Attributes
    ----------------
    order_group: `int` = `0`
        The channel's order group used when sorting channels.
    """
    __slots__ = ('permission_overwrites', 'position', )
    
    @copy_docs(ChannelMetadataGuildBase.__hash__)
    def __hash__(self):
        hash_value = ChannelMetadataGuildBase.__hash__(self)
        
        # permission_overwrites
        permission_overwrites = self.permission_overwrites
        hash_value ^= len(permission_overwrites) << 8
        
        for permission_overwrite in permission_overwrites.values():
            hash_value ^= hash(permission_overwrite)
        
        # position
        hash_value ^= self.position << 24
        
        return hash_value
    
    
    @copy_docs(ChannelMetadataGuildBase._created)
    def _created(self, channel_entity, client):
        try:
            guild = GUILDS[channel_entity.guild_id]
        except KeyError:
            pass
        else:
            guild.channels[channel_entity.id] = channel_entity
    
    
    @copy_docs(ChannelMetadataGuildBase._delete)
    def _delete(self, channel_entity, client):
        try:
            guild = GUILDS[channel_entity.guild_id]
        except KeyError:
            pass
        else:
            try:
                del guild.channels[channel_entity.id]
            except KeyError:
                pass
    
    
    @copy_docs(ChannelMetadataGuildBase._is_equal_same_type)
    def _is_equal_same_type(self, other):
        if not ChannelMetadataGuildBase._is_equal_same_type(self, other):
            return False
        
        if self.permission_overwrites != other.permission_overwrites:
            return False
        
        if self.position != other.position:
            return False
        
        return True
    
    
    @copy_docs(ChannelMetadataGuildBase._update_attributes)
    def _update_attributes(self, data):
        ChannelMetadataGuildBase._update_attributes(self, data)
        
        # permission_overwrites
        self.permission_overwrites = parse_permission_overwrites(data)
        
        # position
        self.position = parse_position(data)
    
    
    @copy_docs(ChannelMetadataGuildBase._difference_update_attributes)
    def _difference_update_attributes(self, data):
        old_attributes = ChannelMetadataGuildBase._difference_update_attributes(self, data)
        
        # permission_overwrites
        permission_overwrites = parse_permission_overwrites(data)
        if self.permission_overwrites != permission_overwrites:
            old_attributes['permission_overwrites'] = self.permission_overwrites
            self.permission_overwrites = permission_overwrites
        
        
        # position
        position = parse_position(data)
        if self.position != position:
            old_attributes['position'] = self.position
            self.position = position
        
        
        return old_attributes
    
    
    @copy_docs(ChannelMetadataGuildBase.to_data)
    def to_data(self, *, defaults = False, include_internals = False):
        data = ChannelMetadataGuildBase.to_data(self, defaults = defaults, include_internals = include_internals)
        
        # position
        put_position_into(self.position, data, defaults)
        
        # permission_overwrites
        put_permission_overwrites_into(self.permission_overwrites, data, defaults)
        
        return data
    
    
    @classmethod
    @copy_docs(ChannelMetadataGuildBase._create_empty)
    def _create_empty(cls):
        self = super(ChannelMetadataGuildMainBase, cls)._create_empty()
        
        self.permission_overwrites = {}
        self.position = 0
        
        return self
    
    
    @copy_docs(ChannelMetadataGuildBase._set_attributes_from_keyword_parameters)
    def _set_attributes_from_keyword_parameters(self, keyword_parameters):
        ChannelMetadataGuildBase._set_attributes_from_keyword_parameters(self, keyword_parameters)
        
        # permission_overwrites
        try:
            permission_overwrites = keyword_parameters.pop('permission_overwrites')
        except KeyError:
            pass
        else:
            self.permission_overwrites = validate_permission_overwrites(permission_overwrites)
        
        # position
        try:
            position = keyword_parameters.pop('position')
        except KeyError:
            pass
        else:
            self.position = validate_position(position)
    
    
    def _get_base_permissions_for(self, channel_entity, user):
        """
        Base permission calculator method. Subclasses call this first, then apply their channel type related changes.
        
        Parameters
        ----------
        channel_entity : ``Channel``
            The channel entity owning the metadata.
        user : ``UserBase``
            The user to calculate it's permissions of.
        
        Returns
        -------
        permissions : ``Permission``
            The calculated permissions.
        """
        guild_id = channel_entity.guild_id
        try:
            guild = GUILDS[guild_id]
        except KeyError:
            return PERMISSION_NONE
        
        if user.id == guild.owner_id:
            return PERMISSION_ALL
        
        if not isinstance(user, ClientUserBase):
            if user.guild_id in guild.channels:
                role_everyone = guild.roles.get(guild_id, None)
                if role_everyone is None:
                    permissions = PERMISSION_NONE
                else:
                    permissions = role_everyone.permissions
                
                # Apply everyone's if applicable
                permission_overwrites = self.permission_overwrites
                try:
                    permission_overwrite_everyone = permission_overwrites[guild_id]
                except KeyError:
                    pass
                else:
                    permissions &= ~permission_overwrite_everyone.deny
                    permissions |= permission_overwrite_everyone.allow
            
                return permissions
            else:
                return PERMISSION_NONE
        
        # Are we in the guild?
        try:
            guild_profile = user.guild_profiles[guild_id]
        except KeyError:
            return PERMISSION_NONE
        
        # Apply everyone's
        role_everyone = guild.roles.get(guild_id, None)
        if role_everyone is None:
            permissions = 0
        else:
            permissions = role_everyone.permissions
        
        roles = guild_profile.roles
        
        # Apply permissions of each role of the user.
        if (roles is not None):
            for role in roles:
                permissions |= role.permissions
        
        # Apply everyone's if applicable
        permission_overwrites = self.permission_overwrites
        try:
            permission_overwrite_everyone = permission_overwrites[guild_id]
        except KeyError:
            pass
        else:
            permissions &= ~permission_overwrite_everyone.deny
            permissions |= permission_overwrite_everyone.allow
        
        # Apply role overwrite
        allow = 0
        deny = 0
        
        if (roles is not None):
            for role in roles:
                try:
                    permission_overwrite_role = permission_overwrites[role.id]
                except KeyError:
                    pass
                else:
                    allow |= permission_overwrite_role.allow
                    deny |= permission_overwrite_role.deny
        
        permissions &= ~deny
        permissions |= allow
        
        # Apply user specific
        try:
            permission_overwrite_user = permission_overwrites[user.id]
        except KeyError:
            pass
        else:
            permissions &= ~permission_overwrite_user.deny
            permissions |= permission_overwrite_user.allow
        
        # Are we admin?
        if permissions & PERMISSION_MASK_ADMINISTRATOR:
            return PERMISSION_ALL
        
        return Permission(permissions)
    
    
    @copy_docs(ChannelMetadataGuildBase._get_permissions_for)
    def _get_permissions_for(self, channel_entity, user):
        result = self._get_base_permissions_for(channel_entity, user)
        if not result & PERMISSION_MASK_VIEW_CHANNEL:
            result = PERMISSION_NONE
        
        return result
    
    
    def _get_base_permissions_for_roles(self, channel_entity, roles):
        """
        Returns the channel permissions of an imaginary user who would have the listed roles. This method is called
        first by subclasses to apply their own related permissions on it.
        
        Parameters
        ----------
        channel_entity : ``Channel``
            The channel entity owning the metadata.
        roles : `tuple` of ``Role``
            The roles to calculate final permissions from.
        
        Returns
        -------
        permissions : ``Permission``
            The calculated permissions.
        
        Notes
        -----
        Partial roles and roles from other guilds as well are ignored.
        """
        guild_id = channel_entity.guild_id
        
        try:
            guild = GUILDS[guild_id]
        except KeyError:
            return PERMISSION_NONE
        
        role_everyone = guild.roles.get(guild_id, None)
        if role_everyone is None:
            permissions = 0
        else:
            permissions = role_everyone.permissions
        
        roles = sorted(roles)
        for role in roles:
            if role.guild_id == guild_id:
                permissions |= role.permissions
        
        if permissions & PERMISSION_MASK_ADMINISTRATOR:
            return PERMISSION_ALL
        
        permission_overwrites = self.permission_overwrites
        try:
            permission_overwrite_everyone = permission_overwrites[guild_id]
        except KeyError:
            pass
        else:
            permissions &= ~permission_overwrite_everyone.deny
            permissions |= permission_overwrite_everyone.allow
        
        allow = 0
        deny = 0
        
        for role in roles:
            try:
                permission_overwrite_role = permission_overwrites[role.id]
            except KeyError:
                pass
            else:
                allow |= permission_overwrite_role.allow
                deny |= permission_overwrite_role.deny
        
        permissions &= ~deny
        permissions |= allow
        
        return Permission(permissions)
    
    
    @copy_docs(ChannelMetadataGuildBase._get_permissions_for_roles)
    def _get_permissions_for_roles(self, channel_entity, roles):
        permissions = self._get_base_permissions_for_roles(channel_entity, roles)
        if not permissions & PERMISSION_MASK_VIEW_CHANNEL:
            permissions = PERMISSION_NONE
        
        return permissions
