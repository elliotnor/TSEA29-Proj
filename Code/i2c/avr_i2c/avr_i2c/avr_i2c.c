#include "avr_i2c.h"

void initI2C()
{
	cli();
	// load address into TWI address register
	TWAR = (0x50 << TWA0);

	// Set SDA(PINC1) and SCL(PINC0) to inputs
	DDRC &= ~(1 << DDC1 | 1 << DDC0); 

	// enable slave transmitter mode
	TWCR = 0;
	TWCR |= (1<<TWEA)|(1<<TWEN)|(1<<TWIE)|(1<<TWINT);
	
	
	sei();
}

void TWILoadData(uint8_t cntr)
{
	TWDR = 10;
}

void dataReceived()
{
	int data = TWDR;
}

void enableTWIInterrupt()
{
	TWCR |= (1 << TWINT);
}

/*
ISR(TWI_vect) //Interrupt TWI
{
	cli();
	
	if(TWSR == 0xA8 || TWSR == 0xB8){ // Master returned ACK, more data wanted. Load TWDR with data to transmit
		PORTA |= (1<<PORTA0);
		DDRC |= (1 << DDC1);
		TWILoadData(cntr);
		cntr = (cntr + 1) % 5;
		PORTA &= ~(1<<PORTA0);
	}
	else if(TWSR == 0xC0 || TWSR == 0xC8){ // Slave finished transmit, Master returned NACK(C0) or ACK(C8
		PORTA |= (1<<PORTA1);
		DDRC |= (1 << DDC1);
		enableTWIInterrupt(); // Transmit is finished, set TWINT flag to 0
		PORTA &= ~(1<<PORTA1);
	}
	else if(TWSR == 0x60 || TWSR == 0x68 || TWSR == 0x70 || TWSR == 0x78){ // TODO: add slave receive condition and what to do then
		//Do nothing, waiting for data
		PORTA |= (1<<PORTA2);
		DDRC &= ~(1 << DDC1); // Set PINC1 to 0
		PORTA &= ~(1<<PORTA2);
	}
	else if(TWSR == 0x80 || TWSR == 0x88){ //data has been received from master
		PORTA |= (1<<PORTA3);
		DDRC &= ~(1 << DDC1);
		dataReceived();
		enableTWIInterrupt();
		PORTA &= ~(1<<PORTA3);
	}
	else{
		//If end up here something is wrong with the code, or if last then finished
		PORTA |= (1<<PORTA4);
		enableTWIInterrupt();
		PORTA &= ~(1<<PORTA4);
	}
	
	enableTWIInterrupt();
	sei();
}*/

//enables pull-up override on all ports
void enable_pullups(){

	DDRA = 0x00;
	DDRB = 0x00;
	DDRC = 0x00;
	DDRD = 0x00;
	
	PINA = 0x00;
	PINB = 0x00;
	PINC = 0x00;
	PIND = 0x00;
	
	PORTA = 0xFF;
	PORTB = 0xFF;
	PORTC = 0xFF;
	PORTD = 0xFF;
	
	MCUCR |= ~(1<<PUD);
}

/*
int main(void)
{
	
	setup_ports();
	
	initI2C();
	PORTA = 0x00;
	DDRA = 0xFF;
	
	cntr = 0;
	
    while(1){
		sei();
    }
}
*/