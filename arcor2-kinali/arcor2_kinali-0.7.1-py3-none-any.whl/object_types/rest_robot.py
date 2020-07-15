from typing import FrozenSet, Iterator, List, Optional

from arcor2.action import action
from arcor2.data.common import ActionMetadata, Joint, Pose, ProjectRobotJoints
from arcor2.data.object_type import MeshFocusAction, Models
from arcor2.exceptions import Arcor2Exception
from arcor2.object_types import Robot
from arcor2.parameter_plugins.relative_pose import RelativePose

from arcor2_kinali.services.robot import MoveTypeEnum, RestRobotService

# TODO how to copy docstrings of methods from service?


class RestRobot(Robot):
    """
    REST interface to the robot.
    """

    def __init__(self, robot_api: RestRobotService, obj_id: str, obj_name: str, pose: Pose,
                 collision_model: Optional[Models] = None) -> None:

        super(RestRobot, self).__init__(obj_id, obj_name, pose, collision_model)
        self.robot_api = robot_api

    def get_end_effectors_ids(self) -> FrozenSet[str]:
        return self.robot_api.get_end_effectors_ids(self.id)

    def get_end_effector_pose(self, end_effector_id: str) -> Pose:  # global pose
        return self.robot_api.get_end_effector_pose(self.id, end_effector_id)

    @staticmethod
    def from_services(robot_api: RestRobotService) -> Iterator["RestRobot"]:

        # TODO what if robot does not support get_robot_pose?
        for robot_id in robot_api.get_robot_ids():
            try:
                yield RestRobot(robot_api, robot_id, robot_id, robot_api.get_robot_pose(robot_id))
            except Arcor2Exception as e:
                print(e)

    def stop(self) -> None:
        self.robot_api.stop(self.id)

    def robot_joints(self) -> List[Joint]:
        return self.robot_api.robot_joints(self.id)

    def move_to_pose(self, end_effector_id: str, target_pose: Pose, speed: float) -> None:
        self.robot_api.move_to_pose(self.id, end_effector_id, target_pose, speed)

    def move_to_joints(self, target_joints: List[Joint], speed: float) -> None:
        self.robot_api.move_to_joints(self.id, target_joints, speed)

    @action
    def move(self, end_effector_id: str, pose: Pose, move_type: MoveTypeEnum, speed: float = 0.5) -> None:
        """
        Moves the robot's end-effector to a specific pose.
        :param end_effector_id: Unique end-effector id.
        :param pose: Target pose.
        :param move_type: Type of move.
        :param speed: Speed of move.
        :return:
        """

        assert 0.0 <= speed <= 1.0

        self.robot_api.move(self.id, end_effector_id, pose, move_type, speed)

    @action
    def move_relative(self, end_effector_id: str, pose: Pose, rel_pose: RelativePose,
                      move_type: MoveTypeEnum, speed: float = 0.5) -> None:
        """
        Moves the robot's end-effector to a specific pose.
        :param end_effector_id: Unique end-effector id.
        :param pose: Target pose.
        :param rel_pose: Relative pose.
        :param move_type: Type of move.
        :param speed: Speed of move.
        :return:
        """

        assert 0.0 <= speed <= 1.0

        self.robot_api.move_relative(self.id, end_effector_id, pose, rel_pose, move_type, speed)

    @action
    def move_relative_joints(self, end_effector_id: str, joints: ProjectRobotJoints,
                             rel_pose: RelativePose, move_type: MoveTypeEnum, speed: float = 0.5) -> None:
        """
        Moves the robot's end-effector relatively to specific joint values.
        :param end_effector_id: Unique end-effector id.
        :param joints: Target joints.
        :param rel_pose: Relative pose.
        :param move_type: Type of move.
        :param speed: Speed of move.
        :return:
        """

        assert 0.0 <= speed <= 1.0

        self.robot_api.move_relative_joints(self.id, end_effector_id, joints, rel_pose, move_type, speed)

    @action
    def set_joints(self, joints: ProjectRobotJoints, move_type: MoveTypeEnum, speed: float = 0.5) -> None:

        assert 0.0 <= speed <= 1.0
        assert self.id == joints.robot_id

        self.robot_api.set_joints(self.id, joints, move_type, speed)

    def inputs(self) -> FrozenSet[str]:
        return self.robot_api.inputs(self.id)

    def outputs(self) -> FrozenSet[str]:
        return self.robot_api.outputs(self.id)

    @action
    def get_input(self, input_id: str) -> float:
        return self.robot_api.get_input(self.id, input_id)

    @action
    def set_output(self, output_id: str, value: float) -> None:
        self.robot_api.set_output(self.id, output_id, value)

    @action
    def get_output(self, output_id: str) -> float:
        return self.robot_api.get_output(self.id, output_id)

    def focus(self, mfa: MeshFocusAction) -> Pose:
        return self.robot_api.focus(mfa)

    def grippers(self) -> FrozenSet[str]:
        return self.robot_api.grippers(self.id)

    @action
    def grip(self, gripper_id: str, position: float = 0.0, speed: float = 0.5, force: float = 0.5) -> None:

        assert 0.0 <= position <= 1.0
        assert 0.0 <= speed <= 1.0
        assert 0.0 <= force <= 1.0

        return self.robot_api.grip(self.id, gripper_id, position, speed, force)

    @action
    def set_opening(self, gripper_id: str, position: float = 1.0, speed: float = 0.5) -> None:

        assert 0.0 <= position <= 1.0
        assert 0.0 <= speed <= 1.0

        self.robot_api.set_opening(self.id, gripper_id, position, speed)

    @action
    def get_gripper_opening(self, gripper_id: str) -> float:
        return self.robot_api.get_gripper_opening(self.id, gripper_id)

    @action
    def is_item_gripped(self, gripper_id: str) -> bool:
        return self.robot_api.is_item_gripped(self.id, gripper_id)

    def suctions(self) -> FrozenSet[str]:
        return self.robot_api.suctions(self.id)

    @action
    def suck(self, suction_id: str) -> None:
        self.robot_api.suck(self.id, suction_id)

    @action
    def release(self, suction_id: str) -> None:
        self.robot_api.release(self.id, suction_id)

    @action
    def is_item_attached(self, suction_id: str) -> bool:
        return self.robot_api.is_item_attached(self.id, suction_id)

    move.__action__ = ActionMetadata(free=True, blocking=True, composite=True, blackbox=True)
    move_relative.__action__ = ActionMetadata(free=True, blocking=True, composite=True, blackbox=True)
    move_relative_joints.__action__ = ActionMetadata(free=True, blocking=True, composite=True, blackbox=True)
    set_joints.__action__ = ActionMetadata(free=True, blocking=True, composite=True, blackbox=True)
    get_input.__action__ = ActionMetadata(free=True, blocking=True, composite=True, blackbox=True)
    set_output.__action__ = ActionMetadata(free=True, blocking=True, composite=True, blackbox=True)
    get_output.__action__ = ActionMetadata(free=True, blocking=True, composite=True, blackbox=True)
    grip.__action__ = ActionMetadata(free=True, blocking=True, composite=True, blackbox=True)
    set_opening.__action__ = ActionMetadata(free=True, blocking=True, composite=True, blackbox=True)
    get_gripper_opening.__action__ = ActionMetadata(free=True, blocking=True, composite=True, blackbox=True)
    is_item_gripped.__action__ = ActionMetadata(free=True, blocking=True, composite=True, blackbox=True)
    suck.__action__ = ActionMetadata(free=True, blocking=True, composite=True, blackbox=True)
    release.__action__ = ActionMetadata(free=True, blocking=True, composite=True, blackbox=True)
    is_item_attached.__action__ = ActionMetadata(free=True, blocking=True, composite=True, blackbox=True)


RestRobot.DYNAMIC_PARAMS = {
    "end_effector_id": (RestRobot.get_end_effectors_ids.__name__, set()),
    "gripper_id": (RestRobot.grippers.__name__, set()),
    "suction_id": (RestRobot.suctions.__name__, set()),
    "input_id": (RestRobot.inputs.__name__, set()),
    "output_id": (RestRobot.outputs.__name__, set())
}

RestRobotService.CANCEL_MAPPING = {
    RestRobot.move.__name__: RestRobot.stop.__name__,
    RestRobot.move_relative.__name__: RestRobot.stop.__name__,
    RestRobot.move_relative_joints.__name__: RestRobot.stop.__name__,
    RestRobot.set_joints.__name__: RestRobot.stop.__name__
}
