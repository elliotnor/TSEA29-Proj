#include "main.h"

//volatile uint8_t sensorCntr;

int main(void)
{
	
	
    
	enable_pullups();
	
	initSensors();
	
	setup_odometer();

	initI2C();

	TWILoadData();
	

	
	
    while (1) 
    {
		sei();
    }
}


ISR(TWI_vect)
{
	cli();
	i2cInterrupt();
	sei();
}

ISR(PCINT0_vect)
{
	cli();
	odometerInterrupt();
	sei();
}

/*

ISR(timerinterrupt){
	h�mta data f�r sensor fetchSensorDataCntr
	fetchSensorDataCntr++;	
}


*/
