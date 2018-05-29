regs = [
    (0x4000000, "DISPCNT", "LCD Control (Read/Write)"),
    (0x4000004, "DISPSTAT", "General LCD Status (Read/Write)"),
    (0x4000006, "VCOUNT", "Vertical Counter (Read only)"),
    (0x4000008, "BG0CNT", "BG0 Control"),
    (0x400000a, "BG1CNT", "BG1 Control"),
    (0x400000c, "BG2CNT", "BG2 Control"),
    (0x400000e, "BG3CNT", "BG3 Control"),
    (0x4000010, "BG0HOFS", "BG0 X-Offset"),
    (0x4000012, "BG0VOFS", "BG0 Y-Offset"),
    (0x4000014, "BG1HOFS", "BG1 X-Offset"),
    (0x4000016, "BG1VOFS", "BG1 Y-Offset"),
    (0x4000018, "BG2HOFS", "BG2 X-Offset"),
    (0x400001a, "BG2VOFS", "BG2 Y-Offset"),
    (0x400001c, "BG3HOFS", "BG3 X-Offset"),
    (0x400001e, "BG3VOFS", "BG3 Y-Offset"),
    (0x4000020, "BG2PA", "BG2 Rotation/Scaling Parameter A (dx)"),
    (0x4000022, "BG2PB", "BG2 Rotation/Scaling Parameter B (dmx)"),
    (0x4000024, "BG2PC", "BG2 Rotation/Scaling Parameter C (dy)"),
    (0x4000026, "BG2PD", "BG2 Rotation/Scaling Parameter D (dmy)"),
    (0x4000028, "BG2X", "BG2 Reference Point X-Coordinate"),
    (0x400002c, "BG2Y", "BG2 Reference Point Y-Coordinate"),
    (0x4000030, "BG3PA", "BG3 Rotation/Scaling Parameter A (dx)"),
    (0x4000032, "BG3PB", "BG3 Rotation/Scaling Parameter B (dmx)"),
    (0x4000034, "BG3PC", "BG3 Rotation/Scaling Parameter C (dy)"),
    (0x4000036, "BG3PD", "BG3 Rotation/Scaling Parameter D (dmy)"),
    (0x4000038, "BG3X", "BG3 Reference Point X-Coordinate"),
    (0x400003c, "BG3Y", "BG3 Reference Point Y-Coordinate"),
    (0x4000040, "WIN0H", "Window 0 Horizontal Dimensions"),
    (0x4000042, "WIN1H", "Window 1 Horizontal Dimensions"),
    (0x4000044, "WIN0V", "Window 0 Vertical Dimensions"),
    (0x4000046, "WIN1V", "Window 1 Vertical Dimensions"),
    (0x4000048, "WININ", "Inside of Window 0 and 1"),
    (0x400004a, "WINOUT", "Inside of OBJ Window & Outside of Windows"),
    (0x400004c, "MOSAIC", "Mosaic Size"),
    (0x4000050, "BLDCNT", "Color Special Effects Selection"),
    (0x4000052, "BLDALPHA", "Alpha Blending Coefficients"),
    (0x4000054, "BLDY", "Brightness (Fade-In/Out) Coefficient"),
    (0x4000060, "SOUND1CNT_L", "Channel 1 Sweep Register"),
    (0x4000062, "SOUND1CNT_H", "Channel 1 Duty/Length/Envelope"),
    (0x4000064, "SOUND1CNT_X", "Channel 1 Frequency/Control"),
    (0x4000068, "SOUND2CNT_L", "Channel 2 Duty/Length/Envelope"),
    (0x400006c, "SOUND2CNT_H", "Channel 2 Frequency/Control"),
    (0x4000070, "SOUND3CNT_L", "Channel 3 Stop/Wave RAM Select"),
    (0x4000072, "SOUND3CNT_H", "Channel 3 Length/Volume"),
    (0x4000074, "SOUND3CNT_X", "Channel 3 Frequency/Control"),
    (0x4000078, "SOUND4CNT_L", "Channel 4 Length/Envelope"),
    (0x400007c, "SOUND4CNT_H", "Channel 4 Frequency/Control"),
    (0x4000080, "SOUNDCNT_L", "Control Stereo/Volume/Enable"),
    (0x4000082, "SOUNDCNT_H", "Control Mixing/DMA Control"),
    (0x4000084, "SOUNDCNT_X", "Control Sound On/Off"),
    (0x4000088, "SOUNDBIAS", "Sound PWM Control"),
    (0x4000090, "WAVE_RAM", "Channel 3 Wave Pattern RAM"),
    (0x40000a0, "FIFO_A", "Channel A FIFO, Data 0-3"),
    (0x40000a4, "FIFO_B", "Channel B FIFO, Data 0-3"),
    (0x40000b0, "DMA0SAD", "DMA 0 Source Address"),
    (0x40000b4, "DMA0DAD", "DMA 0 Destination Address"),
    (0x40000b8, "DMA0CNT_L", "DMA 0 Word Count"),
    (0x40000ba, "DMA0CNT_H", "DMA 0 Control"),
    (0x40000bc, "DMA1SAD", "DMA 1 Source Address"),
    (0x40000c0, "DMA1DAD", "DMA 1 Destination Address"),
    (0x40000c4, "DMA1CNT_L", "DMA 1 Word Count"),
    (0x40000c6, "DMA1CNT_H", "DMA 1 Control"),
    (0x40000c8, "DMA2SAD", "DMA 2 Source Address"),
    (0x40000cc, "DMA2DAD", "DMA 2 Destination Address"),
    (0x40000d0, "DMA2CNT_L", "DMA 2 Word Count"),
    (0x40000d2, "DMA2CNT_H", "DMA 2 Control"),
    (0x40000d4, "DMA3SAD", "DMA 3 Source Address"),
    (0x40000d8, "DMA3DAD", "DMA 3 Destination Address"),
    (0x40000dc, "DMA3CNT_L", "DMA 3 Word Count"),
    (0x40000de, "DMA3CNT_H", "DMA 3 Control"),
    (0x4000100, "TM0CNT_L", "Timer 0 Counter/Reload"),
    (0x4000102, "TM0CNT_H", "Timer 0 Control"),
    (0x4000104, "TM1CNT_L", "Timer 1 Counter/Reload"),
    (0x4000106, "TM1CNT_H", "Timer 1 Control"),
    (0x4000108, "TM2CNT_L", "Timer 2 Counter/Reload"),
    (0x400010a, "TM2CNT_H", "Timer 2 Control"),
    (0x400010c, "TM3CNT_L", "Timer 3 Counter/Reload"),
    (0x400010e, "TM3CNT_H", "Timer 3 Control"),
    (0x4000120, "SIOMULTI0", "SIO Data 0 (Parent)    (Multi-Player Mode; shared with SIODATA32)"),
    (0x4000122, "SIOMULTI1", "SIO Data 1 (1st Child) (Multi-Player Mode)"),
    (0x4000124, "SIOMULTI2", "SIO Data 1 (2nd Child) (Multi-Player Mode)"),
    (0x4000126, "SIOMULTI3", "SIO Data 1 (3rd Child) (Multi-Player Mode)"),
    (0x4000128, "SIOCNT", "SIO Control Register"),
    (0x400012a, "SIOMLT_SEND", "SIO Data (Local of MultiPlayer; shared with SIODATA8)"),
    (0x4000130, "KEYINPUT", "Key Status"),
    (0x4000132, "KEYCNT", "Key Interrupt Control"),
    (0x4000134, "RCNT", "SIO Mode Select/General Purpose Data"),
    (0x4000136, "IR", "Ancient - Infrared Register (Prototypes only)"),
    (0x4000140, "JOYCNT", "SIO JOY BUS Control"),
    (0x4000150, "JOY_RECV", "SIO JOY Bus Receive Data"),
    (0x4000154, "JOY_TRANS", "SIO JOY Bus Transmit Data"),
    (0x4000158, "JOYSTAT", "SIO JOY Bus Receive Status"),
    (0x4000200, "IE", "Interrupt Enable Register"),
    (0x4000202, "IF", "Interrupt Request Flags / IRQ Acknowledge"),
    (0x4000204, "WAITCNT", "Game Pak Waitstate Control"),
    (0x4000208, "IME", "Interrupt Master Enable Register"),
    (0x4000300, "POSTFLG", "Undocumented - Post Boot Flag"),
    (0x4000301, "HALTCNT", "Undocumented - Power Down Control"),
]

for (ea, name, comment) in regs:
    if name:
        idc.MakeName(ea, name)
    if comment:
        idc.MakeRptCmt(ea, comment)