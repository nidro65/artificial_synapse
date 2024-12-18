# Artificial Synapse

This group project was done as part of the assessment of the course Neuromorphic Engineering.

The objective was to model a synapse with a so called memristor.
A memristor is variable resistor whose resistance can be changed by a high voltage programming pulse.

We were able to show Spike-Timing Dependent Plasticity (STDP) and Paired-Pulse Facilitation (PPF), see following pictures.

**Spike Timing Dependent Plasticity**
![STDP](/imgs/stdp_data_not_overlapping.png)
Caption: The graph shows the change in the synapse weight $\Delta w$ depending on the timing difference of the postsynaptic spike versus the presynaptic spike $\Delta T = t_{pre} - t_{post}$. 


**Paired Pulse Facilitation**
![PPF](/imgs/ppf.png)
Caption: Two closely spaced activations yield a smaller synaptic weight increase for the first pulse ($\Delta V_{wdiff} = 185mV$) and an enhanced weight increase for the second pulse ($\Delta V_{wdiff} = 225mV$).

## Get started

 - Open LTSpice
 - Open biolek_diffusive.sub with LTSpice
 - Right click on line 
 
 	.SUBCKT diffusive_biolek TE BE XSV
 	
 - Create symbol (autogenerate)
 - Same for biolek_drift.sub file
 - Open stdp.asc
 - Maybe replace block biolek_drift.asy and biolek_diffusive.asy, the symbols can be found in components (F2) under [autogenerated]
