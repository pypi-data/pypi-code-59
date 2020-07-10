# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flat

import flatbuffers

# /// Contains all rigid body state information.
class RigidBodyTick(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsRigidBodyTick(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = RigidBodyTick()
        x.Init(buf, n + offset)
        return x

    # RigidBodyTick
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # RigidBodyTick
    def Ball(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .BallRigidBodyState import BallRigidBodyState
            obj = BallRigidBodyState()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # RigidBodyTick
    def Players(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .PlayerRigidBodyState import PlayerRigidBodyState
            obj = PlayerRigidBodyState()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # RigidBodyTick
    def PlayersLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def RigidBodyTickStart(builder): builder.StartObject(2)
def RigidBodyTickAddBall(builder, ball): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(ball), 0)
def RigidBodyTickAddPlayers(builder, players): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(players), 0)
def RigidBodyTickStartPlayersVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def RigidBodyTickEnd(builder): return builder.EndObject()
