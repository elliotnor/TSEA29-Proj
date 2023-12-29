/*
gyro.h
Created: 2023-11-06
Author: Hugo Nilsson, hugni385
*/

#include <avr/io.h>

#ifndef GYROSCOPE_H_
#define GYROSCOPE_H_

static int DEGREES_ROTATED; 
static int CURRENT_BEARING;

uint8_t calculateBearing(int data);

void rotate(int degrees);

void resetRotation();

uint8_t readGyro();

/* Will be called upon by initSensors() in the sensormodul-implementation. */
void initGyro();

#endif
