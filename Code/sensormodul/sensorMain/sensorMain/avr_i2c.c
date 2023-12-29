#include "avr_i2c.h"


void initI2C()
{
	cli();
	// load address into TWI address register
	TWAR = (0x60 << TWA0);

	// Set SDA(PINC1) and SCL(PINC0) to inputs
	DDRC &= ~(1 << DDC1 | 1 << DDC0); 

	// enable slave transmitter mode
	TWCR = 0;
	TWCR |= (1<<TWEA)|(1<<TWEN)|(1<<TWIE)|(1<<TWINT);
	
	
	sei();
}

void TWILoadData()
{
	TWDR = getSensorData();
}

void dataReceived()
{
	//int data = TWDR;
	if (TWDR == 0){
		sensorCntr = 0;
	}
	TWILoadData();
}

void enableTWIInterrupt()
{
	TWCR |= (1 << TWINT)|(1<<TWEN);
}

void nextSensor(){
	sensorCntr = (sensorCntr + 1) % 5;
}

//enables pull-up override on all ports
void enable_pullups(){

	DDRA = 0x00;
	DDRB = 0x00;
	DDRC = 0x00;
	DDRD = 0xFF;
	
	PINA = 0x00;
	PINB = 0x00;
	PINC = 0x00;
	PIND = 0x00;
	
	PORTC |= (1<<PINC0)|(1<<PINC1);
	
	PORTC |= (1<<PINC0) | (1<<PINC1);
	
	MCUCR &= ~(1<<PUD);
}


void i2cInterrupt(){
	if(TWSR == 0xA8 || TWSR == 0xB8){ // Master returned ACK, more data wanted. Load TWDR with data to transmit
		
		PORTD |= (1<<PIND4);
		//DDRC |= (1 << DDC1);
		TWILoadData();
		nextSensor();
		//PORTB = sensorCntr;
		
	}
	else if(TWSR == 0xC0 || TWSR == 0xC8){ // Slave finished transmit, Master returned NACK(C0) or ACK(C8
		
		//TWILoadData();
		//nextSensor();
		//DDRC |= (1 << DDC1);
		
	}
	else if(TWSR == 0x60 || TWSR == 0x68 || TWSR == 0x70 || TWSR == 0x78){ 
		
		//DDRC &= ~(1 << DDC1); // Set PINC1 to 0
		
	}
	else if(TWSR == 0x80 || TWSR == 0x88){ //data has been received from master
		
		//DDRC &= ~(1 << DDC1);
		dataReceived();
		
	}
	else{
		//If end up here something is wrong with the code, or if last then finished
	}
	
	enableTWIInterrupt();
}