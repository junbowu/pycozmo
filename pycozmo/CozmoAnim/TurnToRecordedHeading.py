# automatically generated by the FlatBuffers compiler, do not modify

# namespace: CozmoAnim

import flatbuffers

class TurnToRecordedHeading(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsTurnToRecordedHeading(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TurnToRecordedHeading()
        x.Init(buf, n + offset)
        return x

    # TurnToRecordedHeading
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TurnToRecordedHeading
    def TriggerTimeMs(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # TurnToRecordedHeading
    def DurationTimeMs(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # TurnToRecordedHeading
    def OffsetDeg(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

    # TurnToRecordedHeading
    def SpeedDegPerSec(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

    # TurnToRecordedHeading
    def AccelDegPerSec2(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 1000

    # TurnToRecordedHeading
    def DecelDegPerSec2(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 1000

    # TurnToRecordedHeading
    def ToleranceDeg(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 2

    # TurnToRecordedHeading
    def NumHalfRevs(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # TurnToRecordedHeading
    def UseShortestDir(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def TurnToRecordedHeadingStart(builder): builder.StartObject(9)
def TurnToRecordedHeadingAddTriggerTimeMs(builder, triggerTimeMs): builder.PrependUint32Slot(0, triggerTimeMs, 0)
def TurnToRecordedHeadingAddDurationTimeMs(builder, durationTimeMs): builder.PrependUint32Slot(1, durationTimeMs, 0)
def TurnToRecordedHeadingAddOffsetDeg(builder, offsetDeg): builder.PrependInt16Slot(2, offsetDeg, 0)
def TurnToRecordedHeadingAddSpeedDegPerSec(builder, speedDegPerSec): builder.PrependInt16Slot(3, speedDegPerSec, 0)
def TurnToRecordedHeadingAddAccelDegPerSec2(builder, accelDegPerSec2): builder.PrependInt16Slot(4, accelDegPerSec2, 1000)
def TurnToRecordedHeadingAddDecelDegPerSec2(builder, decelDegPerSec2): builder.PrependInt16Slot(5, decelDegPerSec2, 1000)
def TurnToRecordedHeadingAddToleranceDeg(builder, toleranceDeg): builder.PrependUint16Slot(6, toleranceDeg, 2)
def TurnToRecordedHeadingAddNumHalfRevs(builder, numHalfRevs): builder.PrependUint16Slot(7, numHalfRevs, 0)
def TurnToRecordedHeadingAddUseShortestDir(builder, useShortestDir): builder.PrependBoolSlot(8, useShortestDir, 0)
def TurnToRecordedHeadingEnd(builder): return builder.EndObject()
