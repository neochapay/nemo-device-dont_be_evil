#!/bin/sh

# UBports enables camera like this:
# https://gitlab.com/ubports/porting/community-ports/pinephone/-/merge_requests/5/diffs#f40b4251139496d6f8c502a834435af25ed50118
# media-ctl -d /dev/media1 --set-v4l2 '"ov5640 3-004c":0[fmt:UYVY8_2X8/1920x1080@1/15]'

# this part is taken from OpenMandriva
# https://gitlab.com/tui/tui/-/blob/master/cam/camera-setup

case "a$1" in
    a | arear)
        media-ctl -d /dev/media1 --links '"gc2145 3-003c":0->"sun6i-csi":0[0]'
        media-ctl -d /dev/media1 --links '"ov5640 3-004c":0->"sun6i-csi":0[1]'
        media-ctl -d /dev/media1 --set-v4l2 '"ov5640 3-004c":0[fmt:UYVY8_2X8/1280x720]'
    ;;
    afront)
        media-ctl -d /dev/media1 --links '"ov5640 3-004c":0->"sun6i-csi":0[0]'
        media-ctl -d /dev/media1 --links '"gc2145 3-003c":0->"sun6i-csi":0[1]'
        media-ctl -d /dev/media1 --set-v4l2 '"gc2145 3-003c":0[fmt:UYVY8_2X8/1280x720]'
    ;;
esac

# Take a photo: e.g.
#   ffmpeg -s 1280x720 -f video4linux2 -i /dev/video2 -vframes 1 /home/manjaro/Pictures/photo.jpg
#   ffmpeg -s 1280x720 -f video4linux2 -i /dev/video2 -vframes 5 /home/manjaro/Pictures/photo%d.jpg