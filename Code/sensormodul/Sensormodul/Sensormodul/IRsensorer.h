#ifndef IRSENSORER_H_
#define IRSENSORER_H_

#include <avr\io.h>

uint8_t rightIRdata;
uint8_t leftIRdata;
uint8_t fwdIRdata;

extern volatile uint8_t rightDistanceCm();

extern volatile uint8_t leftDistanceCm();

extern volatile uint8_t fwdDistanceCm();



#endif