#include <avr_spi>

int main(){
    // Initialize SPI Slave
	SPI_SlaveInit();
	DDRA |= 0xFF;
	// Enable global interrupts
	sei();

	while (1) {
		PORTA = len;
	}

	return 0;
}