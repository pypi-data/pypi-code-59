import os
from typing import Callable, FrozenSet, List, TYPE_CHECKING, TypeVar

from arcor2 import rest
from arcor2.action import action
from arcor2.data.common import ActionMetadata, Joint, Pose, ProjectRobotJoints
from arcor2.data.object_type import MeshFocusAction, Model3dType, Models
from arcor2.object_types import Generic
from arcor2.parameter_plugins.relative_pose import RelativePose
from arcor2.services.robot_service import RobotService

from arcor2_kinali.data.robot import MoveRelativeJointsParameters, MoveRelativeParameters, MoveTypeEnum
from arcor2_kinali.services import systems


URL = os.getenv("REST_ROBOT_SERVICE_URL", "http://127.0.0.1:13000")

# mypy work-around by GvR (https://github.com/python/mypy/issues/5107#issuecomment-529372406)
if TYPE_CHECKING:
    F = TypeVar('F', bound=Callable)

    def lru_cache(maxsize: int = 128, typed: bool = False) -> Callable[[F], F]:
        pass
else:
    from functools import lru_cache


class RestRobotService(RobotService):
    """
    REST interface to the robot service.
    """

    def __init__(self, configuration_id: str):

        super(RestRobotService, self).__init__(configuration_id)
        systems.create(URL, self)

    def cleanup(self) -> None:
        systems.destroy(URL)

    @staticmethod
    def get_configuration_ids() -> FrozenSet[str]:
        return systems.systems(URL)

    def add_collision_model(self, model: Models, pose: Pose) -> None:
        """
        Adds arbitrary collision model to the collision scene.
        :param model: Box, Sphere, Cylinder, Mesh
        :param pose: Pose of the collision object.
        :return:

        Example usage:

        >>> from arcor2.data.object_type import Box
        >>> from arcor2.data.common import Pose, Position. Orientation
        >>> box = Box("UniqueBoxId", 0.1, 0.1, 0.1)
        >>> robot_service.add_collision_model(box, Pose(Position(1, 0, 0), Orientation(0, 0, 0, 1)))

        """

        model_id = model.id
        params = model.to_dict()
        del params["id"]
        params[model.__class__.__name__.lower() + "Id"] = model_id

        # TODO temporary hack
        if model.type() == Model3dType.MESH:
            params["mesh_scale_x"] = 1.0
            params["mesh_scale_y"] = 1.0
            params["mesh_scale_z"] = 1.0
            params["transform_id"] = "world"

        rest.put(f"{URL}/collisions/{model.type().value}", pose, params)

    def remove_collision_model_id(self, model_id: str) -> None:

        rest.delete(f"{URL}/collisions/{model_id}")

    def add_collision(self, obj: Generic) -> None:
        """
        Adds object's collision model to the collision scene.
        :param obj: Scene object.
        :return:
        """

        if not obj.collision_model or obj.collision_model.type() == Model3dType.NONE:
            return

        self.add_collision_model(obj.collision_model, obj.pose)

    def remove_collision(self, obj: Generic) -> None:
        if not obj.collision_model or obj.collision_model.type() == Model3dType.NONE:
            return

        self.remove_collision_model_id(obj.collision_model.id)

    def clear_collisions(self) -> None:

        for coll_id in rest.get_list_primitive(f"{URL}/collisions", str):
            rest.delete(f"{URL}/collisions/{coll_id}")

    def move_to_pose(self, robot_id: str, end_effector_id: str, target_pose: Pose, speed: float) -> None:

        rest.put(f"{URL}/robots/{robot_id}/endeffectors/{end_effector_id}/move", target_pose,
                 {"moveType": MoveTypeEnum.AVOID_COLLISIONS.value, "speed": speed})

    def move_to_joints(self, robot_id: str, target_joints: List[Joint], speed: float) -> None:

        rest.put(f"{URL}/robots/{robot_id}/joints", target_joints,
                 {"moveType": MoveTypeEnum.AVOID_COLLISIONS.value, "speed": speed})

    @lru_cache()
    def get_robot_ids(self) -> FrozenSet[str]:
        return frozenset(rest.get_data(f"{URL}/robots"))

    def get_robot_pose(self, robot_id: str) -> Pose:
        return rest.get(f"{URL}/robots/{robot_id}/pose", Pose)

    def stop(self, robot_id: str) -> None:
        rest.put(f"{URL}/robots/{robot_id}/stop")

    def robot_joints(self, robot_id: str) -> List[Joint]:
        return rest.get_list(f"{URL}/robots/{robot_id}/joints", Joint)

    @lru_cache()
    def get_end_effectors_ids(self, robot_id: str) -> FrozenSet[str]:
        return frozenset(rest.get_data(f"{URL}/robots/{robot_id}/endeffectors"))

    def get_end_effector_pose(self, robot_id: str, end_effector_id: str) -> Pose:
        return rest.get(f"{URL}/robots/{robot_id}/endeffectors/{end_effector_id}/pose", Pose)

    @action
    def move(self, robot_id: str, end_effector_id: str, pose: Pose, move_type: MoveTypeEnum,
             speed: float = 0.5) -> None:
        """
        Moves the robot's end-effector to a specific pose.
        :param robot_id: Unique robot id.
        :param end_effector_id: Unique end-effector id.
        :param pose: Target pose.
        :param move_type: Type of move.
        :param speed: Speed of move.
        :return:
        """

        assert 0.0 <= speed <= 1.0

        rest.put(f"{URL}/robots/{robot_id}/endeffectors/{end_effector_id}/move", pose,
                 {"moveType": move_type.value, "speed": speed})

    @action
    def move_relative(self, robot_id: str, end_effector_id: str, pose: Pose, rel_pose: RelativePose,
                      move_type: MoveTypeEnum, speed: float = 0.5) -> None:
        """
        Moves the robot's end-effector to a specific pose.
        :param robot_id: Unique robot id.
        :param end_effector_id: Unique end-effector id.
        :param pose: Target pose.
        :param rel_pose: Relative pose.
        :param move_type: Type of move.
        :param speed: Speed of move.
        :return:
        """

        assert 0.0 <= speed <= 1.0

        body = MoveRelativeParameters(pose, rel_pose.position, rel_pose.orientation)
        rest.put(f"{URL}/robots/{robot_id}/endeffectors/{end_effector_id}/moveRelative", body,
                 {"moveType": move_type.value, "speed": speed})

    @action
    def move_relative_joints(self, robot_id: str, end_effector_id: str, joints: ProjectRobotJoints,
                             rel_pose: RelativePose, move_type: MoveTypeEnum, speed: float = 0.5) -> None:
        """
        Moves the robot's end-effector relatively to specific joint values.
        :param robot_id: Unique robot id.
        :param end_effector_id: Unique end-effector id.
        :param joints: Target joints.
        :param rel_pose: Relative pose.
        :param move_type: Type of move.
        :param speed: Speed of move.
        :return:
        """

        assert 0.0 <= speed <= 1.0

        body = MoveRelativeJointsParameters(joints.joints, rel_pose.position, rel_pose.orientation)
        rest.put(f"{URL}/robots/{robot_id}/endeffectors/{end_effector_id}/moveRelativeJoints", body,
                 {"moveType": move_type.value, "speed": speed})

    @action
    def set_joints(self, robot_id: str, joints: ProjectRobotJoints, move_type: MoveTypeEnum,
                   speed: float = 0.5) -> None:

        assert 0.0 <= speed <= 1.0
        assert robot_id == joints.robot_id
        rest.put(f"{URL}/robots/{robot_id}/joints", joints.joints, {"moveType": move_type.value, "speed": speed})

    @lru_cache()
    def inputs(self, robot_id: str) -> FrozenSet[str]:
        return frozenset(rest.get_data(f"{URL}/robots/{robot_id}/inputs"))

    @lru_cache()
    def outputs(self, robot_id: str) -> FrozenSet[str]:
        return frozenset(rest.get_data(f"{URL}/robots/{robot_id}/outputs"))

    @action
    def get_input(self, robot_id: str, input_id: str) -> float:
        super(RestRobotService, self).get_input(robot_id, input_id)
        return rest.get_primitive(f"{URL}/robots/{robot_id}/inputs/{input_id}", float)

    @action
    def set_output(self, robot_id: str, output_id: str, value: float) -> None:

        assert 0.0 <= value <= 1.0

        super(RestRobotService, self).set_output(robot_id, output_id, value)
        rest.put(f"{URL}/robots/{robot_id}/outputs/{output_id}", params={"value": value})

    @action
    def get_output(self, robot_id: str, output_id: str) -> float:
        return rest.get_primitive(f"{URL}/robots/{robot_id}/outputs/{output_id}", float)

    def focus(self, mfa: MeshFocusAction) -> Pose:
        return rest.put(f"{URL}/utils/focus", mfa, data_cls=Pose)

    @lru_cache()
    def grippers(self, robot_id: str) -> FrozenSet[str]:
        return frozenset(rest.get_data(f"{URL}/robots/{robot_id}/grippers"))

    @action
    def grip(self, robot_id: str, gripper_id: str, position: float = 0.0, speed: float = 0.5, force: float = 0.5) -> \
            None:

        assert 0.0 <= position <= 1.0
        assert 0.0 <= speed <= 1.0
        assert 0.0 <= force <= 1.0

        rest.put(f"{URL}/robots/{robot_id}/grippers/{gripper_id}/grip", params={"position": position,
                                                                                "speed": speed,
                                                                                "force": force})

    @action
    def set_opening(self, robot_id: str, gripper_id: str, position: float = 1.0, speed: float = 0.5) -> None:

        assert 0.0 <= position <= 1.0
        assert 0.0 <= speed <= 1.0

        rest.put(f"{URL}/robots/{robot_id}/grippers/{gripper_id}/opening", params={"position": position,
                                                                                   "speed": speed})

    @action
    def get_gripper_opening(self, robot_id: str, gripper_id: str) -> float:

        return rest.get_primitive(f"{URL}/robots/{robot_id}/grippers/{gripper_id}/opening", float)

    @action
    def is_item_gripped(self, robot_id: str, gripper_id: str) -> bool:
        return rest.get_primitive(f"{URL}/robots/{robot_id}/grippers/{gripper_id}/gripped", bool)

    @lru_cache()
    def suctions(self, robot_id: str) -> FrozenSet[str]:
        return frozenset(rest.get_data(f"{URL}/robots/{robot_id}/suctions"))

    @action
    def suck(self, robot_id: str, suction_id: str) -> None:
        rest.put(f"{URL}/robots/{robot_id}/suctions/{suction_id}/suck")

    @action
    def release(self, robot_id: str, suction_id: str) -> None:
        rest.put(f"{URL}/robots/{robot_id}/suctions/{suction_id}/release")

    @action
    def is_item_attached(self, robot_id: str, suction_id: str) -> bool:
        return rest.get_primitive(f"{URL}/robots/{robot_id}/suctions/{suction_id}/attached", bool)

    move.__action__ = ActionMetadata(free=True, blocking=True)
    move_relative.__action__ = ActionMetadata(free=True, blocking=True)
    move_relative_joints.__action__ = ActionMetadata(free=True, blocking=True)
    set_joints.__action__ = ActionMetadata(free=True, blocking=True)
    get_input.__action__ = ActionMetadata(free=True, blocking=True)
    set_output.__action__ = ActionMetadata(free=True, blocking=True)
    get_output.__action__ = ActionMetadata(free=True, blocking=True)
    grip.__action__ = ActionMetadata(free=True, blocking=True)
    set_opening.__action__ = ActionMetadata(free=True, blocking=True)
    get_gripper_opening.__action__ = ActionMetadata(free=True, blocking=True)
    is_item_gripped.__action__ = ActionMetadata(free=True, blocking=True)
    suck.__action__ = ActionMetadata(free=True, blocking=True)
    release.__action__ = ActionMetadata(free=True, blocking=True)
    is_item_attached.__action__ = ActionMetadata(free=True, blocking=True)


RestRobotService.DYNAMIC_PARAMS = {
    "robot_id": (RestRobotService.get_robot_ids.__name__, set()),
    "end_effector_id": (RestRobotService.get_end_effectors_ids.__name__, {"robot_id"}),
    "gripper_id": (RestRobotService.grippers.__name__, {"robot_id"}),
    "suction_id": (RestRobotService.suctions.__name__, {"robot_id"}),
    "input_id": (RestRobotService.inputs.__name__, {"robot_id"}),
    "output_id": (RestRobotService.outputs.__name__, {"robot_id"})
}

RestRobotService.CANCEL_MAPPING = {
    RestRobotService.move.__name__: RestRobotService.stop.__name__,
    RestRobotService.move_relative.__name__: RestRobotService.stop.__name__,
    RestRobotService.move_relative_joints.__name__: RestRobotService.stop.__name__,
    RestRobotService.set_joints.__name__: RestRobotService.stop.__name__
}
