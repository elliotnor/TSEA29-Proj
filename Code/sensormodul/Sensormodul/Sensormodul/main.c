
#include <avr/io.h>
#include <avr/interrupt.h>
#include "sensorhub.h"

uint8_t data_IR_1;
uint8_t data_IR_2;
uint8_t data_IR_3;
uint8_t data_gyro;

/* loop for testing */

int main() {
	initSensors();
	
	DDRB |= 0xFF;
	
	while(1) {
		data_IR_1 = getRightDistance();
		data_IR_2 = getLeftDistance();
		data_IR_3 = getFwdDistance();
		data_gyro = getGyroData();
		
	}
	return 0;
}

/*
int port = 0;



/* Initialize all sensors and ADC
void initSensors() {
	/* Initialize Gyroscope
	initGyro();

	/* Initialize IR-Sensors (distance) 
	// initDistance();

	/* Initialize the AD Converter 
	initADC();

}

/* Read the initial gyro-data for future reference. This should be around 124 
void readInitialGyro() {
	ADMUX &= 0xE0;
	ADMUX |= 0b00000011;
	adc_start();
	uint16_t GYRO_DATA = adc_read();
	return;
}


/* Main-loop sequentially fetches data from ADC ports 0-3. 
int main() {

	/* Configure ports. 
	DDRB = 0xFF;

	
	/* Initialize sensors. 
	initSensors();
	readInitialGyro();

	while(1) {
		
		switch(port) {
			/* IR Sensor 1. A21. 10-80cm. 
			case 0:
			ADMUX &= 0xE0; /* Clear the ADMUX to make sure we don't look at the wrong input. 
			ADMUX |= 0b00000000; /* Read from ADC Port 0. 
			adc_start(); /* Set MUX0 bit to 1 in ADMUX, which tells the ADC to convert data from PORTA 0 (40). 
			data_IR_1 = adc_read(); /* Store result of conversion. 
			PORTB = data_IR_1;
			// length = to_mm(data_IR_1); // DOES NOT WORK.
			port = 1;
			
			break;
			
			/* IR Sensor 2. 4-30cm. 
			case 1:
			ADMUX &= 0xE0; /* Clear the ADMUX to make sure we don't look at the wrong input.  
			ADMUX |= 0b00000001;
			adc_start(); /* Set MUX1 bit to 1. Reads data from PORTA 1 (39)  
			data_IR_2 = adc_read();
			PORTB = data_IR_2;
			port = 2;
			
			break;
			
			/* IR Sensor 3. 4-30cm. 
			case 2:
			ADMUX &= 0xE0; /* Clear the ADMUX to make sure we don't look at the wrong input. 
			ADMUX |= 0b00000010;
			adc_start(); /* PORTA 2 (38) 
			data_IR_3 = adc_read();
			PORTB = data_IR_3;
			port = 3;
			
			break;
			
			/* Gyroscope 
			case 3:
			ADMUX &= 0xE0; /* Clear the ADMUX to make sure we don't look at the wrong input. 
			ADMUX |= 0b00000011; /* Read from PINA3 
			adc_start(); /* PORTA3 (37), gyro 
			data_gyro = adc_read();
			PORTB = data_gyro;
			port = MUX0; /* Start over again  
			break;
			
		}
		
	}
} */