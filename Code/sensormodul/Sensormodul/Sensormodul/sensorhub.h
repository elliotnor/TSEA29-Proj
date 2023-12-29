#include <avr/io.h>

#ifndef SENSORHUB_H_
#define SENSORHUB_H_

#include "gyroscope.h"
#include "adconverter.h"
#include "IRsensorer.h"

uint8_t GYRO_DATA;
uint8_t rightDistance;
uint8_t leftDistance;
uint8_t fwdDistance;

void initSensors();

uint8_t getGyroData();

uint8_t getRightDistance();

uint8_t getLeftDistance();

uint8_t getFwdDistance();

#endif