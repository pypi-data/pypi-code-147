from . import _init_wpilib

# TODO: robotpy-build subpackage bug
from wpimath._controls._controls import trajectory as _

# autogenerated by 'robotpy-build create-imports wpilib'
from ._wpilib import (
    ADIS16448_IMU,
    ADIS16470_IMU,
    ADXL345_I2C,
    ADXL345_SPI,
    ADXL362,
    ADXRS450_Gyro,
    AddressableLED,
    AnalogAccelerometer,
    AnalogEncoder,
    AnalogGyro,
    AnalogInput,
    AnalogOutput,
    AnalogPotentiometer,
    AnalogTrigger,
    AnalogTriggerOutput,
    AnalogTriggerType,
    BuiltInAccelerometer,
    CAN,
    CANData,
    CANStatus,
    Color,
    Color8Bit,
    Compressor,
    CompressorConfigType,
    Counter,
    DataLogManager,
    DMC60,
    DSControlWord,
    DigitalGlitchFilter,
    DigitalInput,
    DigitalOutput,
    DigitalSource,
    DoubleSolenoid,
    DriverStation,
    DutyCycle,
    DutyCycleEncoder,
    Encoder,
    Field2d,
    FieldObject2d,
    I2C,
    IterativeRobotBase,
    Jaguar,
    Joystick,
    LiveWindow,
    Mechanism2d,
    MechanismLigament2d,
    MechanismObject2d,
    MechanismRoot2d,
    MotorControllerGroup,
    MotorSafety,
    NidecBrushless,
    Notifier,
    PS4Controller,
    PWM,
    PWMMotorController,
    PWMSparkMax,
    PWMTalonFX,
    PWMTalonSRX,
    PWMVenom,
    PWMVictorSPX,
    PneumaticHub,
    PneumaticsBase,
    PneumaticsControlModule,
    PneumaticsModuleType,
    PowerDistribution,
    Preferences,
    Relay,
    RobotBase,
    RobotController,
    RobotState,
    RuntimeType,
    SD540,
    SPI,
    SendableBuilderImpl,
    SendableChooser,
    SendableChooserBase,
    SensorUtil,
    SerialPort,
    Servo,
    SmartDashboard,
    Solenoid,
    Spark,
    SynchronousInterrupt,
    Talon,
    TimedRobot,
    Timer,
    TimesliceRobot,
    Tracer,
    Ultrasonic,
    Victor,
    VictorSP,
    Watchdog,
    XboxController,
    getCurrentThreadPriority,
    getDeployDirectory,
    getErrorMessage,
    getOperatingDirectory,
    getTime,
    setCurrentThreadPriority,
    wait,
)

__all__ = [
    "ADIS16448_IMU",
    "ADIS16470_IMU",
    "ADXL345_I2C",
    "ADXL345_SPI",
    "ADXL362",
    "ADXRS450_Gyro",
    "AddressableLED",
    "AnalogAccelerometer",
    "AnalogEncoder",
    "AnalogGyro",
    "AnalogInput",
    "AnalogOutput",
    "AnalogPotentiometer",
    "AnalogTrigger",
    "AnalogTriggerOutput",
    "AnalogTriggerType",
    "BuiltInAccelerometer",
    "CAN",
    "CANData",
    "CANStatus",
    "Color",
    "Color8Bit",
    "Compressor",
    "CompressorConfigType",
    "Counter",
    "DataLogManager",
    "DMC60",
    "DSControlWord",
    "DigitalGlitchFilter",
    "DigitalInput",
    "DigitalOutput",
    "DigitalSource",
    "DoubleSolenoid",
    "DriverStation",
    "DutyCycle",
    "DutyCycleEncoder",
    "Encoder",
    "Field2d",
    "FieldObject2d",
    "I2C",
    "IterativeRobotBase",
    "Jaguar",
    "Joystick",
    "LiveWindow",
    "Mechanism2d",
    "MechanismLigament2d",
    "MechanismObject2d",
    "MechanismRoot2d",
    "MotorControllerGroup",
    "MotorSafety",
    "NidecBrushless",
    "Notifier",
    "PS4Controller",
    "PWM",
    "PWMMotorController",
    "PWMSparkMax",
    "PWMTalonFX",
    "PWMTalonSRX",
    "PWMVenom",
    "PWMVictorSPX",
    "PneumaticHub",
    "PneumaticsBase",
    "PneumaticsControlModule",
    "PneumaticsModuleType",
    "PowerDistribution",
    "Preferences",
    "Relay",
    "RobotBase",
    "RobotController",
    "RobotState",
    "RuntimeType",
    "SD540",
    "SPI",
    "SendableBuilderImpl",
    "SendableChooser",
    "SendableChooserBase",
    "SensorUtil",
    "SerialPort",
    "Servo",
    "SmartDashboard",
    "Solenoid",
    "Spark",
    "SynchronousInterrupt",
    "Talon",
    "TimedRobot",
    "Timer",
    "TimesliceRobot",
    "Tracer",
    "Ultrasonic",
    "Victor",
    "VictorSP",
    "Watchdog",
    "XboxController",
    "getCurrentThreadPriority",
    "getDeployDirectory",
    "getErrorMessage",
    "getOperatingDirectory",
    "getTime",
    "setCurrentThreadPriority",
    "wait",
]

# Error reporting
from ._impl.report_error import reportError, reportWarning

__all__ += ["reportError", "reportWarning"]

del _init_wpilib

from .cameraserver import CameraServer
from .deployinfo import getDeployData

try:
    from .version import version as __version__
except ImportError:
    __version__ = "master"

from ._impl.main import run

__all__ += ["CameraServer", "run"]
