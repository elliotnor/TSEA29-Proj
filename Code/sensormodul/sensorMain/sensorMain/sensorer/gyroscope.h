
#ifndef GYROSCOPE_H_
#define GYROSCOPE_H_

#include <avr/io.h>
#include <util/delay.h>
#include "adconverter.h"

uint8_t calculateBearing(int data);

void rotate(int degrees);

void resetRotation();

uint8_t readGyro();

/* Will be called upon by initSensors() in the sensormodul-implementation. */
void initGyro();

#endif
