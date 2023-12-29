#include "avr_spi.h"

void SPI_SlaveInit(void)
{
    /* Set MISO output, all others input */
   	DDRB |= (1 << DDB6);
    /* Enable SPI */
    SPCR = (1<<SPE);
}
char SPI_SlaveReceive(void)
{
    /* Wait for reception complete */
    while(!(SPSR & (1<<SPIF)))
    ;
    /* Return Data Register */
    return SPDR;
}