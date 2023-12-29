#include <avr/io.h>

#include <stdio.h>
#include <util/delay.h>
#include <stdbool.h>
#include <avr/interrupt.h>

#include "steering.h"
#include "avr_i2c.h"





void databehandling() {
	uint8_t data = TWDR;
	int speed = 90;
	
	switch(data) {
		case 0x00:
			stop();
			break;
		
		case 0x01:
			set_speed(speed);
			set_direction(FORWARD);
			//_delay_ms(500);
			break;
		
		case 0x02:
			set_speed(speed);
			set_direction(BACKWARD);
			//_delay_ms(500);
			break;
		
		case 0x03:
			set_speed(speed);
			rotate_right();
			//_delay_ms(500);
			break;
		
		case 0x04:
			set_speed(speed);
			rotate_left();
			//_delay_ms(500);
			break;
			
		case 0x05:
			set_speed(speed);
			turn_right();
			_delay_ms(500);
			break;
			
		case 0x06:
			set_speed(speed);
			turn_left();
			_delay_ms(500);
			break;
			
		default:
			break;
	}
}

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
	else if(TWSR == 0x60 || TWSR == 0x68 || TWSR == 0x70 || TWSR == 0x78){
		//Do nothing, waiting for data
		PORTA |= (1<<PORTA2);
		DDRC &= ~(1 << DDC1); // Set PINC1 to 0
		PORTA &= ~(1<<PORTA2);
	}
	else if(TWSR == 0x80 || TWSR == 0x88){ //data has been received from master
		PORTA |= (1<<PORTA3);
		DDRC &= ~(1 << DDC1);
		databehandling();
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
}


int main(void) {
	
	enable_pullups();

	DDRA = 0xFF;
	
	initI2C();

	pwm_init();
	set_speed(100);
	set_direction(FORWARD);
	_delay_ms(1000);
	stop();
	
	sei();
	
	while(1){
		sei();
	}
	
	return 0;
}
