# Image of Nemo with Glacier UX for PinePhone

![](https://sun9-41.userapi.com/c200620/v200620091/3a74e/sbKlDMbA0eA.jpg)


## Links for download
[Version 0.8](https://yadi.sk/d/VAbtKV-Hnql60g)

[Version 0.6](https://yadi.sk/d/gwZoHr9OmdHp3g)

[Version 0.5](https://yadi.sk/d/fj3oodP3Kl1QIg)

[Version 0.3](https://yadi.sk/d/uZgrqVtCrH5Ifg)

## How to flash
You need 2+ GB SD card to fash nemomobile. 
### Prepare sd card
Use GParted or any other tool to create the following EXT4 partitions:

* boot: Holds the mainline kernel Image and Device Tree files
* data: Holds the Nemo rootFS 

GParted will ask you to leave the first MB free of the SD card when creating the first partition, this is correct. This 1 MB will be used to store the U-boot boot loader.

_Note: Make sure you have a msdos partition table! If not, the U-boot flashing will make partition table unusable (in case of GPT for example)!_

### Burn U-boot to your SD card
Copy the compiled U-boot bootloader to the first sector on your SD card:
```sudo dd if=u-boot-sunxi-with-spl.bin of=/dev/sdX bs=8k seek=1```

### Unpack rootFS 

Unpack downloaded archive into data part of you sd-card. After copy all file from /boot dir into /boot partion of sdcard

## Know bugs
* Voicecall not work
* Sounds not work
* Cameras not work

## Contribute
* All hw probles as MR to this project
* UI/UX here https://github.com/nemomobile-ux/

## Chat
* NemoMobile in telegram: https://t.me/NemoMobile
* nemomobile chat on freenode
