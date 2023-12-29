
#ifndef GYROSCOPE_H_
#define GYROSCOPE_H_

<<<<<<<< HEAD:sensormodul/sensorMain/sensorMain/sensorer/gyroscope.h
static int DEGREES_ROTATED; 
static int CURRENT_BEARING;
========
#include <avr/io.h>
#include <util/delay.h>
#include "adconverter.h"
>>>>>>>> sensorIntegration:sensormodul/sensorMain/sensorMain/gyroscope.h

uint8_t calculateBearing(int data);

void rotate(int degrees);

void resetRotation();

uint8_t readGyro();

/* Will be called upon by initSensors() in the sensormodul-implementation. */
void initGyro();

#endif
