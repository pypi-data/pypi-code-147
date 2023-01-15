# -*- coding: utf-8 -*-


from brainpy._src.math.arraycompatible import (
  full as full,
  full_like as full_like,
  eye as eye,
  identity as identity,
  diag as diag,
  tri as tri,
  tril as tril,
  triu as triu,
  real as real,
  imag as imag,
  conj as conj,
  conjugate as conjugate,
  ndim as ndim,
  isreal as isreal,
  isscalar as isscalar,
  add as add,
  reciprocal as reciprocal,
  negative as negative,
  positive as positive,
  multiply as multiply,
  divide as divide,
  power as power,
  subtract as subtract,
  true_divide as true_divide,
  floor_divide as floor_divide,
  float_power as float_power,
  fmod as fmod,
  mod as mod,
  modf as modf,
  divmod as divmod,
  remainder as remainder,
  abs as abs,
  exp as exp,
  exp2 as exp2,
  expm1 as expm1,
  log as log,
  log10 as log10,
  log1p as log1p,
  log2 as log2,
  logaddexp as logaddexp,
  logaddexp2 as logaddexp2,
  lcm as lcm,
  gcd as gcd,
  arccos as arccos,
  arccosh as arccosh,
  arcsin as arcsin,
  arcsinh as arcsinh,
  arctan as arctan,
  arctan2 as arctan2,
  arctanh as arctanh,
  cos as cos,
  cosh as cosh,
  sin as sin,
  sinc as sinc,
  sinh as sinh,
  tan as tan,
  tanh as tanh,
  deg2rad as deg2rad,
  hypot as hypot,
  rad2deg as rad2deg,
  degrees as degrees,
  radians as radians,
  round as round,
  around as around,
  round_ as round_,
  rint as rint,
  floor as floor,
  ceil as ceil,
  trunc as trunc,
  fix as fix,
  prod as prod,
  sum as sum,
  diff as diff,
  median as median,
  nancumprod as nancumprod,
  nancumsum as nancumsum,
  nanprod as nanprod,
  nansum as nansum,
  cumprod as cumprod,
  cumsum as cumsum,
  ediff1d as ediff1d,
  cross as cross,
  trapz as trapz,
  isfinite as isfinite,
  isinf as isinf,
  isnan as isnan,
  signbit as signbit,
  copysign as copysign,
  nextafter as nextafter,
  ldexp as ldexp,
  frexp as frexp,
  convolve as convolve,
  sqrt as sqrt,
  cbrt as cbrt,
  square as square,
  absolute as absolute,
  fabs as fabs,
  sign as sign,
  heaviside as heaviside,
  maximum as maximum,
  minimum as minimum,
  fmax as fmax,
  fmin as fmin,
  interp as interp,
  clip as clip,
  angle as angle,
  bitwise_and as bitwise_and,
  bitwise_not as bitwise_not,
  bitwise_or as bitwise_or,
  bitwise_xor as bitwise_xor,
  invert as invert,
  left_shift as left_shift,
  right_shift as right_shift,
  equal as equal,
  not_equal as not_equal,
  greater as greater,
  greater_equal as greater_equal,
  less as less,
  less_equal as less_equal,
  array_equal as array_equal,
  isclose as isclose,
  allclose as allclose,
  logical_and as logical_and,
  logical_not as logical_not,
  logical_or as logical_or,
  logical_xor as logical_xor,
  all as all,
  any as any,
  alltrue as alltrue,
  sometrue as sometrue,
  shape as shape,
  size as size,
  reshape as reshape,
  ravel as ravel,
  moveaxis as moveaxis,
  transpose as transpose,
  swapaxes as swapaxes,
  concatenate as concatenate,
  stack as stack,
  vstack as vstack,
  hstack as hstack,
  dstack as dstack,
  column_stack as column_stack,
  split as split,
  dsplit as dsplit,
  hsplit as hsplit,
  vsplit as vsplit,
  tile as tile,
  repeat as repeat,
  unique as unique,
  append as append,
  flip as flip,
  fliplr as fliplr,
  flipud as flipud,
  roll as roll,
  atleast_1d as atleast_1d,
  atleast_2d as atleast_2d,
  atleast_3d as atleast_3d,
  expand_dims as expand_dims,
  squeeze as squeeze,
  sort as sort,
  argsort as argsort,
  argmax as argmax,
  argmin as argmin,
  argwhere as argwhere,
  nonzero as nonzero,
  flatnonzero as flatnonzero,
  where as where,
  searchsorted as searchsorted,
  extract as extract,
  count_nonzero as count_nonzero,
  max as max,
  min as min,
  amax as amax,
  amin as amin,
  array_split as array_split,
  meshgrid as meshgrid,
  vander as vander,
  nonzero as nonzero,
  where as where,
  tril_indices as tril_indices,
  tril_indices_from as tril_indices_from,
  triu_indices as triu_indices,
  triu_indices_from as triu_indices_from,
  take as take,
  select as select,
  nanmin as nanmin,
  nanmax as nanmax,
  ptp as ptp,
  percentile as percentile,
  nanpercentile as nanpercentile,
  quantile as quantile,
  nanquantile as nanquantile,
  median as median,
  average as average,
  mean as mean,
  std as std,
  var as var,
  nanmedian as nanmedian,
  nanmean as nanmean,
  nanstd as nanstd,
  nanvar as nanvar,
  corrcoef as corrcoef,
  correlate as correlate,
  cov as cov,
  histogram as histogram,
  bincount as bincount,
  digitize as digitize,
  bartlett as bartlett,
  blackman as blackman,
  hamming as hamming,
  hanning as hanning,
  kaiser as kaiser,
  e as e,
  pi as pi,
  inf as inf,
  dot as dot,
  vdot as vdot,
  inner as inner,
  outer as outer,
  kron as kron,
  matmul as matmul,
  trace as trace,
  dtype as dtype,
  finfo as finfo,
  iinfo as iinfo,
  uint8 as uint8,
  uint16 as uint16,
  uint32 as uint32,
  uint64 as uint64,
  int8 as int8,
  int16 as int16,
  int32 as int32,
  int64 as int64,
  float16 as float16,
  float32 as float32,
  float64 as float64,
  complex64 as complex64,
  complex128 as complex128,
  product as product,
  row_stack as row_stack,
  apply_over_axes as apply_over_axes,
  apply_along_axis as apply_along_axis,
  array_equiv as array_equiv,
  array_repr as array_repr,
  array_str as array_str,
  block as block,
  broadcast_arrays as broadcast_arrays,
  broadcast_shapes as broadcast_shapes,
  broadcast_to as broadcast_to,
  compress as compress,
  cumproduct as cumproduct,
  diag_indices as diag_indices,
  diag_indices_from as diag_indices_from,
  diagflat as diagflat,
  diagonal as diagonal,
  einsum as einsum,
  einsum_path as einsum_path,
  geomspace as geomspace,
  gradient as gradient,
  histogram2d as histogram2d,
  histogram_bin_edges as histogram_bin_edges,
  histogramdd as histogramdd,
  i0 as i0,
  in1d as in1d,
  indices as indices,
  insert as insert,
  intersect1d as intersect1d,
  iscomplex as iscomplex,
  isin as isin,
  ix_ as ix_,
  lexsort as lexsort,
  load as load,
  save as save,
  savez as savez,
  mask_indices as mask_indices,
  msort as msort,
  nan_to_num as nan_to_num,
  nanargmax as nanargmax,
  setdiff1d as setdiff1d,
  nanargmin as nanargmin,
  pad as pad,
  poly as poly,
  polyadd as polyadd,
  polyder as polyder,
  polyfit as polyfit,
  polyint as polyint,
  polymul as polymul,
  polysub as polysub,
  polyval as polyval,
  resize as resize,
  rollaxis as rollaxis,
  roots as roots,
  rot90 as rot90,
  setxor1d as setxor1d,
  tensordot as tensordot,
  trim_zeros as trim_zeros,
  union1d as union1d,
  unravel_index as unravel_index,
  unwrap as unwrap,
  take_along_axis as take_along_axis,
  can_cast as can_cast,
  choose as choose,
  copy as copy,
  frombuffer as frombuffer,
  fromfile as fromfile,
  fromfunction as fromfunction,
  fromiter as fromiter,
  fromstring as fromstring,
  get_printoptions as get_printoptions,
  iscomplexobj as iscomplexobj,
  isneginf as isneginf,
  isposinf as isposinf,
  isrealobj as isrealobj,
  issubdtype as issubdtype,
  issubsctype as issubsctype,
  iterable as iterable,
  packbits as packbits,
  piecewise as piecewise,
  printoptions as printoptions,
  set_printoptions as set_printoptions,
  promote_types as promote_types,
  ravel_multi_index as ravel_multi_index,
  result_type as result_type,
  sort_complex as sort_complex,
  unpackbits as unpackbits,
  delete as delete,
  add_docstring as add_docstring,
  add_newdoc as add_newdoc,
  add_newdoc_ufunc as add_newdoc_ufunc,
  array2string as array2string,
  asanyarray as asanyarray,
  ascontiguousarray as ascontiguousarray,
  asfarray as asfarray,
  asscalar as asscalar,
  common_type as common_type,
  disp as disp,
  genfromtxt as genfromtxt,
  loadtxt as loadtxt,
  info as info,
  issubclass_ as issubclass_,
  place as place,
  polydiv as polydiv,
  put as put,
  putmask as putmask,
  safe_eval as safe_eval,
  savetxt as savetxt,
  savez_compressed as savez_compressed,
  show_config as show_config,
  typename as typename,
  copyto as copyto,
  matrix as matrix,
  asmatrix as asmatrix,
  mat as mat,
)
