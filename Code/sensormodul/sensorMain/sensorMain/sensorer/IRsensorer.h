#ifndef IRSENSORER_H_
#define IRSENSORER_H_

#include <avr/io.h>

uint8_t rightIRdata;
uint8_t leftIRdata;
uint8_t fwdIRdata;

extern volatile uint8_t readRightData();

extern volatile uint8_t readLeftData();

extern volatile uint8_t readFwdData();



#endif