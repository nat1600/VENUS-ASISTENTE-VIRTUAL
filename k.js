var waves = new SineWaves({
  el: document.getElementById('waves'),
  
  speed: 4,
  
  ease: 'SineInOut',
  
  wavesWidth: '75%',
  
  waves: [
    {
      timeModifier: 4,
      lineWidth: 1,
      amplitude: -35,
      wavelength: 35
    },
    {
      timeModifier: 2,
      lineWidth: 1,
      amplitude: -20,
      wavelength: 40
    },
    {
      timeModifier: 1,
      lineWidth: 1,
      amplitude: -40,
      wavelength: 40
    },
		{
      timeModifier: 3,
      lineWidth: 1,
      amplitude: 50,
      wavelength: 50
    },
    {
      timeModifier: 0.5,
      lineWidth: 1,
      amplitude: -70,
      wavelength: 70
    },
    {
      timeModifier: 1.3,
      lineWidth: 1,
      amplitude: -50,
      wavelength: 50
    }
  ],
 
  // Called on window resize
  resizeEvent: function() {
    var gradient = this.ctx.createLinearGradient(0, 0, this.width, 0);
    gradient.addColorStop(0,"rgba(20, 227, 255,0.80)");
    gradient.addColorStop(0.5,"rgba(255, 25, 260, 0.90)");
    gradient.addColorStop(1,"rgba(255, 255, 25, 0.80");
    
    var index = -1;
    var length = this.waves.length;
	  while(++index < length){
      this.waves[index].strokeStyle = gradient;
    }
    
    // Clean Up
    index = void 0;
    length = void 0;
    gradient = void 0;
  }
});