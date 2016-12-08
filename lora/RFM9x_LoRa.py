RegFifo = 0x00 # FIFO read/write access
RegOpMode = 0x01 # Operating mode &  LoRa TM / FSK selection
RegFrfMsb = 0x06 # RF Carrier Frequency, Most Significant Bits
RegFrfMid = 0x07 # RF Carrier Frequency, Intermediate Bits
RegFrfLsb = 0x08 # RF Carrier Frequency, Least Significant Bits
RegPaConfig = 0x09 # PA selection and Output Power control
RegPaRamp = 0x0A # Control of PA ramp time, low phase noise PLL
RegOcp = 0x0B # Over Current Protection control
RegLna = 0x0C # LNA settings
RegFifoAddrPtr = 0x0D # FIFO SPI pointer
RegFifoTxBaseAddr = 0x0E # Start Tx data
RegFifoRxBaseAddr = 0x0F # Start Rx data
RegIrqFlags = 0x10 # LoRa state flags
RegIrqFlagsMask = 0x11 # Optional IRQ flag mask
RegFreqIfMsb = 0x12 # IF Frequency - MSB
RegFreqIFLsb = 0x13 # IF Frequency - LSB
RegSymbTimeoutMsb = 0x14 # Receiver timeout value - MSB
RegSymbTimeoutLsb = 0x15 # Receiver timeout value - LSB
RegTxCfg = 0x16 # LoRa transmit parameters
RegPreambleMsb = 0x18 # Size of preamble - MSB
RegPreambleLsb = 0x19 # Size of preamble - LSB
RegModulationCfg = 0x1A # Modem PHY config
RegRfMode = 0x1B # Test register
RegHopPeriod = 0x1C # FHSS Hop period
RegNbRxBytes = 0x1D # Number of received bytes
RegRxHeaderInfo = 0x1E # Value of the calculated frequency error Info from last header
RegRxHeaderCntValue = 0x1F # Number of valid headers received
RegRxPacketCntValue = 0x20 # Number of valid packets received
RegModemStat = 0x21 # Live LoRa modem status
RegPktSnrValue = 0x22 # Estimation of last packet SNR
RegRssiValue = 0x23 # Current RSSI
RegPktRssiValue = 0x24 # RSSi of last packet
RegHopChannel = 0x25 # FHSS start channel
RegRxDataAddr = 0x26 # LoRa rx data pointer
RegDioMapping1 = 0x40 # Mapping of pins DIO0 to DIO3
RegDioMapping2 = 0x41 # Mapping of pins DIO4 and DIO5, ClkOut frequency
RegVersion = 0x42 # Hope RF ID relating the silicon revision
RegTcxo = 0x4B # TCXO or XTAL input setting
RegPaDac = 0x4D # Higher power settings of the PA
RegFormerTemp = 0x5B # Stored temperature during the former IQ Calibration
RegAgcRef = 0x61 # Adjustment of the AGC thresholds
RegAgcThresh1 = 0x62 # Adjustment of the AGC thresholds
RegAgcThresh2 = 0x63 # Adjustment of the AGC thresholds
RegAgcThresh3 = 0x64 # Adjustment of the AGC thresholds