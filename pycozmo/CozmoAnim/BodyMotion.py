# automatically generated by the FlatBuffers compiler, do not modify

# namespace: CozmoAnim

import flatbuffers

class BodyMotion(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsBodyMotion(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = BodyMotion()
        x.Init(buf, n + offset)
        return x

    # BodyMotion
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # BodyMotion
    def TriggerTimeMs(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # BodyMotion
    def DurationTimeMs(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # BodyMotion
    def RadiusMm(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # BodyMotion
    def Speed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

def BodyMotionStart(builder): builder.StartObject(4)
def BodyMotionAddTriggerTimeMs(builder, triggerTimeMs): builder.PrependUint32Slot(0, triggerTimeMs, 0)
def BodyMotionAddDurationTimeMs(builder, durationTimeMs): builder.PrependUint32Slot(1, durationTimeMs, 0)
def BodyMotionAddRadiusMm(builder, radiusMm): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(radiusMm), 0)
def BodyMotionAddSpeed(builder, speed): builder.PrependInt16Slot(3, speed, 0)
def BodyMotionEnd(builder): return builder.EndObject()
