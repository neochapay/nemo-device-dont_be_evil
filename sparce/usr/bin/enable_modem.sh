#!/bin/bash

for i in 35 68 232
do
        echo $i > /sys/class/gpio/export
        echo out > /sys/class/gpio/gpio$i/direction
done

echo 0 > /sys/class/gpio/gpio68/value
echo 1 > /sys/class/gpio/gpio232/value

echo 1 > /sys/class/gpio/gpio35/value && sleep 2 && echo 0 > /sys/class/gpio/gpio35/value