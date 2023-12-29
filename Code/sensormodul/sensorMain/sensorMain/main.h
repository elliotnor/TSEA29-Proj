#include <avr/io.h>
#include <avr/interrupt.h>
#include "avr_i2c.h"
#include "odometer.h"
#include "sensorhub.h"




int main(void);


ISR(TWI_vect);

ISR(PCINT0_vect);

/*

ISR(timerinterrupt);

*/
