LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)
LOCAL_MODULE := android.hardware.audio.service.mediatek.rc
LOCAL_MODULE_TAGS  := optional
LOCAL_MODULE_CLASS := ETC
LOCAL_MODULE_PATH := $(TARGET_OUT_VENDOR_ETC)/init
LOCAL_SRC_FILES := $(LOCAL_MODULE)
include $(BUILD_PREBUILT)

LOCAL_PATH := hardware/interfaces/audio/common/all-versions/default/service

include $(CLEAR_VARS)
LOCAL_MODULE := android.hardware.audio.service.mediatek
LOCAL_REQUIRED_MODULES := android.hardware.audio.service.mediatek.rc
LOCAL_MODULE_RELATIVE_PATH := hw
LOCAL_VENDOR_MODULE := true
LOCAL_MULTILIB := 32

LOCAL_SRC_FILES := \
    service.cpp

LOCAL_CFLAGS := \
    -Wall \
    -Wextra \
    -Werror

LOCAL_SHARED_LIBRARIES := \
    libcutils \
    libbinder \
    libbinder_ndk \
    libhidlbase \
    liblog \
    libutils \
    libhardware

include $(BUILD_EXECUTABLE)

# Copy Dolby audio service
LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)
LOCAL_MODULE := android.hardware.audio.service.mediatek
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_CLASS := EXECUTABLES
LOCAL_SRC_FILES := proprietary/bin/hw/android.hardware.audio.service.mediatek
LOCAL_MODULE_PATH := $(TARGET_OUT_VENDOR)/bin/hw
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
LOCAL_MODULE := libmediaplayerservice
LOCAL_MODULE_CLASS := SHARED_LIBRARIES
LOCAL_SRC_FILES := proprietary/lib/libmediaplayerservice.so
LOCAL_MODULE_PATH := $(TARGET_OUT)/lib
include $(BUILD_PREBUILT)
