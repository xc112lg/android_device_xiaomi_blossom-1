#
# Copyright (C) 2023 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/non_ab_device.mk)

# Inherit from device makefile.
$(call inherit-product, device/xiaomi/blossom/device.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Malloc
PRODUCT_DISABLE_SCUDO := true

#Bootanimation
scr_resolution := 720
TARGET_BOOT_ANIMATION_RES := 720

#Product
PRODUCT_NAME := lineage_blossom
PRODUCT_DEVICE := blossom
PRODUCT_MANUFACTURER := Xiaomi
PRODUCT_BRAND := Redmi
PRODUCT_GMS_CLIENTID_BASE := android-xiaomi

#Sign build with private key
-include vendor/lineage-priv/keys/keys.mk

#Enable Blur
TARGET_ENABLE_BLUR := true
TARGET_SUPPORTS_BLUR := true

#Bomb AudioFx
BOMB_AUDIOFX := true

#Bomb malloc and aperture
TARGET_DISABLE_MATLOG := true
PRODUCT_NO_CAMERA := true

# always append time of day
LINEAGE_VERSION_APPEND_TIME_OF_DAY := true

#Include some stuff
TARGET_INCLUDE_VIA := false
TARGET_INCLUDE_REVAMPED := false
TARGET_FACE_UNLOCK_SUPPORTED := true
TARGET_SUPPORTS_QUICK_TAP := true
TARGET_INCLUDE_DOLBY := true

#Overwrite build fingerprint
PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="blossom-user 16 BP4A.260105.004.E1 14587043 release-keys" \
    BuildFingerprint=xiaomi/blossom/blossom:16/BP4A.260105.004.E1/14587043:user/release-keys \
    DeviceProduct=xiaomi

#Mist stuff
#Mist maintainer
MISTOS_MAINTAINER := HaiKito

#Gms
TARGET_DEFAULT_PIXEL_LAUNCHER := false
TARGET_INCLUDE_LAWNCHAIR := false
BYPASS_CHARGE_SUPPORTED := false
