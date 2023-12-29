#include "adconverter.h"


//Single conversion ADFR, ADIF blir ett när konverteringen är klar

void initADC(void)
{
	//Setup ADC
	DDRA = 0x00; // Enable pins A as input, otherwise ADC doesn't accept analog signals coming in.
	ADMUX = (3<<REFS0) | (1<<ADLAR);
	ADMUX &= ~(0x0F); // Clear lower nibble of ADMUX register, makes sure that we don't read from the wrong port.
	ADCSRA = (1<<ADEN) | (0<<ADATE) | (0<<ADIE) | (1<<ADPS1) | (1<<ADPS2); // (3<<ADPS0); // AD Enabled. Interrupts enabled. Prescaler value of 64.

	ADCSRA |= (1<<ADSC); //Do an initial conversion
}

/* DO NOT USE THIS FUNCTION. Only for reference. */
bool is_ready(void){
	return !(ADCSRA & (1<<ADSC));
}

void adc_start(){
	ADCSRA |= (1<<ADSC);
	return;
}

uint8_t adc_read(void){
	while (!(ADCSRA & (1<<ADIF))); {
		/* wait for conversion to finish */
	}
	return (ADCH);
}

