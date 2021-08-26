# Copyright (C) 2017-2020 The LineageOS Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import common
import re

def FullOTA_InstallEnd(info):
  input_zip = info.input_zip
  OTA_UpdateFirmware(info)
  OTA_InstallEnd(info, input_zip)
  return

def IncrementalOTA_InstallEnd(info):
  input_zip = info.target_zip
  OTA_UpdateFirmware(info)
  OTA_InstallEnd(info, input_zip)
  return

def OTA_UpdateFirmware(info):
  info.script.AppendExtra('ui_print("Flashing firmware images");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/abl.img", "/dev/block/bootdevice/by-name/abl_a");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/abl.img", "/dev/block/bootdevice/by-name/abl_b");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/abl.img", "/dev/block/bootdevice/by-name/ablbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/aop.img", "/dev/block/bootdevice/by-name/aop_a");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/aop.img", "/dev/block/bootdevice/by-name/aop_b");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/aop.img", "/dev/block/bootdevice/by-name/aopbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/bluetooth.img", "/dev/block/bootdevice/by-name/bluetooth_a");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/bluetooth.img", "/dev/block/bootdevice/by-name/bluetooth_b");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/bluetooth.img", "/dev/block/bootdevice/by-name/bluetoothbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/imagefv.img", "/dev/block/bootdevice/by-name/imagefv_a");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/imagefv.img", "/dev/block/bootdevice/by-name/imagefv_b");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/imagefv.img", "/dev/block/bootdevice/by-name/imagefvbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/cmnlib.img", "/dev/block/bootdevice/by-name/cmnlib_a");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/cmnlib.img", "/dev/block/bootdevice/by-name/cmnlib_b");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/cmnlib.img", "/dev/block/bootdevice/by-name/cmnlibbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/cmnlib64.img", "/dev/block/bootdevice/by-name/cmnlib64_a");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/cmnlib64.img", "/dev/block/bootdevice/by-name/cmnlib64_b");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/cmnlib64.img", "/dev/block/bootdevice/by-name/cmnlib64bak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/devcfg.img", "/dev/block/bootdevice/by-name/devcfg_a");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/devcfg.img", "/dev/block/bootdevice/by-name/devcfg_b");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/devcfg.img", "/dev/block/bootdevice/by-name/devcfgbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/dsp.img", "/dev/block/bootdevice/by-name/dsp_a");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/dsp.img", "/dev/block/bootdevice/by-name/dsp_b");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/dsp.img", "/dev/block/bootdevice/by-name/dspbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/hyp.img", "/dev/block/bootdevice/by-name/hyp_a");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/hyp.img", "/dev/block/bootdevice/by-name/hyp_b");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/hyp.img", "/dev/block/bootdevice/by-name/hypbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/keymaster.img", "/dev/block/bootdevice/by-name/keymaster_a");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/keymaster.img", "/dev/block/bootdevice/by-name/keymaster_b");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/keymaster.img", "/dev/block/bootdevice/by-name/keymasterbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/qupv3fw.img", "/dev/block/bootdevice/by-name/qupfw_a");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/qupv3fw.img", "/dev/block/bootdevice/by-name/qupfw_b");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/qupv3fw.img", "/dev/block/bootdevice/by-name/qupfwbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/modem.img", "/dev/block/bootdevice/by-name/modem_a");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/modem.img", "/dev/block/bootdevice/by-name/modem_b");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/modem.img", "/dev/block/bootdevice/by-name/modembak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/uefisecapp.img", "/dev/block/bootdevice/by-name/uefisecapp_a");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/uefisecapp.img", "/dev/block/bootdevice/by-name/uefisecapp_b");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/uefisecapp.img", "/dev/block/bootdevice/by-name/uefisecappbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/tz.img", "/dev/block/bootdevice/by-name/tz_a");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/tz.img", "/dev/block/bootdevice/by-name/tz_b");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/tz.img", "/dev/block/bootdevice/by-name/tzbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/xbl.img", "/dev/block/bootdevice/by-name/xbl_a");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/xbl.img", "/dev/block/bootdevice/by-name/xbl_b");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/xbl.img", "/dev/block/bootdevice/by-name/xblbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/xbl_config.img", "/dev/block/bootdevice/by-name/xbl_config_a");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/xbl_config.img", "/dev/block/bootdevice/by-name/xbl_config_b");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/xbl_config.img", "/dev/block/bootdevice/by-name/xbl_configbak");')

def AddImage(info, input_zip, basename, dest):
  name = basename
  path = "IMAGES/" + name
  if path not in input_zip.namelist():
    return

  data = input_zip.read(path)
  common.ZipWriteStr(info.output_zip, name, data)
  info.script.Print("Patching {} image unconditionally...".format(dest.split('/')[-1]))
  info.script.AppendExtra('package_extract_file("%s", "%s");' % (name, dest))

def OTA_InstallEnd(info, input_zip):
  AddImage(info, input_zip, "vbmeta.img", "/dev/block/bootdevice/by-name/vbmeta_a")
  AddImage(info, input_zip, "vbmeta.img", "/dev/block/bootdevice/by-name/vbmeta_b")
  AddImage(info, input_zip, "vbmeta_system.img", "/dev/block/bootdevice/by-name/vbmeta_system_a")
  AddImage(info, input_zip, "vbmeta_system.img", "/dev/block/bootdevice/by-name/vbmeta_system_b")
  AddImage(info, input_zip, "dtbo.img", "/dev/block/bootdevice/by-name/dtbo_a")
  AddImage(info, input_zip, "dtbo.img", "/dev/block/bootdevice/by-name/dtbo_b")
  return
