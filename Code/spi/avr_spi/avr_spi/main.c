#include "avr_spi_copy.h"

void SPI_SlaveInit(void)
{
	/* Set MISO output, all others input */
	DDRB |= (1 << DDB6);
	/* Enable SPI */
	SPCR = (1<<SPIE) | (1<<SPE);
}
char SPI_SlaveReceive(void)
{
	/* Wait for reception complete */
	while(!(SPSR & (1<<SPIF))){}
	/* Return Data Register */
	return SPDR;
}

int main(){
	SPI_SlaveInit();
	sei();
	DDRA = 1;
	while(1){

		SPDR = 0x10;
	}
}

ISR(SPI_STC_vect) { //after transaction, SPIF = 1
	PORTA = 1;
		
	PORTA = 0;
}