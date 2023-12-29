
#ifndef AVR_I2C_H_
#define AVR_I2C_H_

#include <avr/io.h>
#include <avr/interrupt.h>
#include "sensorMux.h"

void initI2C(void);

void TWILoadData();

void dataReceived();

void enable_pullups(void);

void i2cInterrupt();

#endif