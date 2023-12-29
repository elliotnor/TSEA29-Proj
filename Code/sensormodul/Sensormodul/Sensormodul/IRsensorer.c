#include <math.h>
#include "IRsensorer.h"

uint8_t rightIRdata;
uint8_t leftIRdata;
uint8_t fwdIRdata;

uint8_t convertSides(uint8_t data) {
	uint8_t convertedVal = 42.6*exp((-0.0248*data));
	return convertedVal;
}

/* Functions for reading distance in each direction. Also converts to centimeters. */

/* GP2Y0A41SK. 4-30 CM. Right facing sensor. */
uint8_t rightDistanceCm() {
	ADMUX &= 0xE0; /* Clear the ADMUX to make sure we don't look at the wrong input. */
	ADMUX |= 0b00000000; /* Read from ADC Port 0. */
	
	adc_start(); /* Set MUX0 bit to 1 in ADMUX, which tells the ADC to convert data from PORTA 0 (40). */
	
	rightIRdata = adc_read();
	
	uint8_t right_distance_cm = convertSides(rightIRdata);
	
	return right_distance_cm;
}

/* GP2Y0A41SK. 4-30 CM. Right facing sensor. */
uint8_t leftDistanceCm() {
	ADMUX &= 0xE0; /* Clear the ADMUX to make sure we don't look at the wrong input.  */
	ADMUX |= 0b00000001;
	
	adc_start(); /* Set MUX1 bit to 1. Reads data from PORTA 1 (39)  */
	
	leftIRdata = adc_read();
	
	uint8_t left_distance_cm = convertSides(leftIRdata);
	
	return left_distance_cm;
}

uint8_t convertFwd(uint8_t data) {
	uint8_t convertedVal = 3876*pow(data, -1.27);
	return convertedVal;
}

/* GP2Y0A21. 10-80 CM. Forward facing sensors. */
uint8_t fwdDistanceCm() {
	ADMUX &= 0xE0; /* Clear the ADMUX to make sure we don't look at the wrong input. */
	ADMUX |= 0b00000010;
	
	adc_start(); /* PORTA 2 (38) */
	
	fwdIRdata = adc_read();
	
	uint8_t fwd_distance_cm = convertFwd(fwdIRdata);
	
	return fwd_distance_cm;
}

