/*
 * odometer.c
 *
 * Created: 2023-11-15 11:26:34
 * Author : ellno907
 */ 

#include <avr/io.h>
#include <avr/interrupt.h>


volatile uint16_t odometer_cntr;


//L�ngd p� pinne = 5,8*pi/40 cm = 0.4555cm = 4.55mm
//Diameter 5,8cm
//Antal gropar 40
 

void setup_odometer(){
	
	reset_odometer_cntr();
	
	//IVSEL spelar ingen roll, likas� IVCE?
	MCUCR = 0;
	
	//Set external interrupts to generate pulse on rising edge
	EICRA = 0;
	EICRA |= (1<<ISC01)|(1<<ISC00);
	
	//Enable PCINT0n external interrupts
	EIMSK = 0;
	EIMSK |= (1<<INT0);
	
	//clear interrupt flags
	EIFR |= (1<<INTF0);
	
	//Enable interrupts
	PCICR = 0;
	PCICR |= (1<<PCIE0);
	
	/*
	//clear interrupt flag
	PCIFR |= (1<<PCIF0); 
	*/
	
	//Set PIN7 to external interrupt
	PCMSK0 |= (1<<PCINT7);
	
}

void reset_odometer_cntr(){
	odometer_cntr = 0;
}

int main(void)
{
    /* Replace with your application code */
	
	cli();
	
	setup_odometer();
	
	DDRB = 0xFF;
	DDRA = 0;
	
	sei();
	
	
    while (1) 
    {
		sei();
    }
}

ISR(PCINT0_vect){
	cli();
	if( (PINA & (1 << PINA7)) == 0b10000000 )
	{
		odometer_cntr = odometer_cntr +1;
		PORTB = odometer_cntr;
	}
	EIFR |= (1<<INTF0);	
	sei();
}