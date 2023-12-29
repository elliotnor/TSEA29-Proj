
#include "gyroscope.h"



uint8_t readGyro() {
	ADMUX &= 0xE0; /* Clear the ADMUX to make sure we don't look at the wrong input. */
	ADMUX |= 0b00000011; /* ADC Port 3 */ 
	adc_start(); /* Start a conversion */
	uint8_t data = adc_read();
	return data;
}

/* Initializes the gyroscope. Called upon in sensormodule.c on start-up.*/
void initGyro() {
    _delay_ms(200); /* Gyro requires ~150ms for startup. */

    /* Bearing is equal to the initial data sent from the gyro. This will be used as a reference point. Value given by readInitialGyro() in sensormodul.c */
    // CURRENT_BEARING = GYRO_DATA; // Should give value around 124.
}

