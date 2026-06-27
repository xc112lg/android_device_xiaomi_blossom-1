LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)
LOCAL_MODULE := android.hardware.audio.service.mediatek.rc
LOCAL_MODULE_TAGS  := optional
LOCAL_MODULE_CLASS := ETC
LOCAL_MODULE_PATH := $(TARGET_OUT_VENDOR_ETC)/init
LOCAL_SRC_FILES := $(LOCAL_MODULE)
include $(BUILD_PREBUILT)

# Dolby Media Player Service Library
include $(CLEAR_VARS)
LOCAL_MODULE := libmediaplayerservice
LOCAL_MODULE_CLASS := SHARED_LIBRARIES
LOCAL_MODULE_TAGS := optional
LOCAL_VENDOR_MODULE := true
LOCAL_MULTILIB := both
LOCAL_SRC_FILES_64 := proprietary/lib/libmediaplayerservice.so
LOCAL_SRC_FILES_32 := proprietary/lib/libmediaplayerservice.so
LOCAL_MODULE_PATH := $(TARGET_OUT_VENDOR_SHARED_LIBRARIES)
include $(BUILD_PREBUILT)

# Note: android.hardware.audio.service.mediatek is already defined in 
# hardware/interfaces/audio/common/all-versions/default/service
# Do not redefine it here to avoid duplicate module errors
