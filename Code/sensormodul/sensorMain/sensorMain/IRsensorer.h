#ifndef IRSENSORER_H_
#define IRSENSORER_H_

#include "adconverter.h"
#include <math.h>
#include <avr/io.h>

uint8_t rightIRdata;
uint8_t leftIRdata;
uint8_t fwdIRdata;

uint8_t readRightData();

uint8_t readLeftData();

uint8_t readFwdData();



#endif