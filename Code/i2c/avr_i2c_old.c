//#include <utils.h>
#include <avr/interrupt.h>
#include <inttypes.h>
#include <avr/wdt.h>
#include <avr/io.h>
#include <util/twi.h>


volatile int counter_I2c = 0;
#define SCK DDB5

uint8_t cntr;
uint8_t test[] = {1,2,3,4,5};
uint8_t data;

void initI2C()
{
	// load address into TWI address register
    TWAR = (0x11 << TWA0);

	// enable slave transmitter mode
    TWCR = (1<<TWEA)|(1<<TWEN)|(1<<TWIE);
	
	DDRC |= ~(1 << DDC1 | 1 << DDC0); // Set SDA(PINC1) and SCL(PINC0) to inputs
}

void TWILoadData(uint8_t cntr)
{
    TWDR = test[cntr];     //test code, should be data from sensor
}

void dataReceived()
{
    data = TWDR;
}

void enableTWIInterrupt()
{
    TWCR |= (1 << TWINT);
}

ISR(TWI_vect) //Interrupt TWI
{
    cli();
    PORTA = 1;
    if(TWSR == 0xA8 || TWSR == 0xB8){ // Master returned ACK, more data wanted. Load TWDR with data to transmit
		DDRC |= (1 << DDC1);
		TWILoadData(cntr);
        cntr = cntr + 1 % 5;   
    }
    else if(TWSR == 0xC0 || TWSR == 0xC8){ // Slave finished transmit, Master returned NACK(C0) or ACK(C8
		DDRC |= (1 << DDC1); 
		enableTWIInterrupt(); // Transmit is finished, set TWINT flag to 0
    }
    else if(TWSR == 0x60 || TWSR == 0x68 || TWSR == 0x70 || TWSR == 0x78){ // TODO: add slave receive condition and what to do then
        //Do nothing, waiting for data
		DDRC &= ~(1 << DDC1); // Set PINC1 to 0
	}
    else if(TWSR == 0x80 || TWSR == 0x88){
		DDRC &= ~(1 << DDC1);
		dataReceived();
        enableTWIInterrupt();
    }
    else{
        //If end up here something is wrong with the code
		DDRD = 0xff;
        PORTD = 1; //Error ping on PORTC1
        enableTWIInterrupt();
        PORTD = 0;
    }
    PORTA = 0;
    sei();
}
