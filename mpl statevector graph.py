QUBIT_COUNT = 2
BASIS_VECTOR_COUNT = 2 ** QUBIT_COUNT
RUN_COUNT = 100
from typing import Literal
from IPython.display import display_latex,display
from matplotlib.figure import Figure
from matplotlib.pyplot import bar, figure
from numpy import sqrt

from bitstring import Bits,BitArray
from qiskit.quantum_info.states.random import random_statevector,Statevector

# random_state = random_statevector(dims=BASIS_VECTOR_COUNT)
# display(random_state.draw('repr'))
# display(random_state.draw('text'))
# display(random_state.draw('latex'))
# display(random_state.draw('latex_source'))
# display(random_state.draw('qsphere'))
# display(random_state.draw('hinton'))
# display(random_state.draw('bloch'))
# display(random_state.draw('city'))

counts:dict[Bits,int]={}
for i in range(BASIS_VECTOR_COUNT):
	istr = f"0b{i:0{QUBIT_COUNT}b}"
	ibits = Bits(istr)
	counts[ibits] = RUN_COUNT // (BASIS_VECTOR_COUNT)
	
statevector_bar_chart : Figure = figure(figsize=(BASIS_VECTOR_COUNT, 3))

statevector_bar_chart.text(x=0,y=1,s="Statevector Estimation", usetex=True, fontdict={"size":16, "weight":"bold"})
for i in range(BASIS_VECTOR_COUNT):
	istr = f"0b{i:0{QUBIT_COUNT}b}"
	ibits = Bits(istr)
	count = counts[ibits]
	bar(x=i, height=sqrt(count/RUN_COUNT), width=.5, bottom=0, data=count, color="blue")
statevector_bar_chart_axes = statevector_bar_chart.axes[0]
# Y Axis: Amplitudes
statevector_bar_chart_axes.set_xlabel(xlabel=f"\\par\n {QUBIT_COUNT}-Qubit Computational\nBasis Vectors", usetex=True, fontdict={"size":16, "weight":"bold", "math_fontfamily":"cm"})
statevector_bar_chart_axes.tick_params(axis="x", which="both", width=0)
statevector_bar_chart_axes.set_xticks(range(BASIS_VECTOR_COUNT), [rf"\[\vert{i:0{QUBIT_COUNT}b}\rangle\]" for i in range(BASIS_VECTOR_COUNT)], usetex=True, fontsize=12)
# Y Axis: Amplitudes
statevector_bar_chart_axes.set_ylabel(ylabel="Probability Amplitude", usetex=False, fontdict={"size":16, "weight":"bold", "math_fontfamily":"cm"})
for label in statevector_bar_chart_axes.get_yticklabels():
	label.set_usetex(True)
	label.set_math_fontfamily("dejavusans")
	label.set_math_fontfamily("dejavuserif")
	label.set_math_fontfamily("cm")
	label.set_math_fontfamily("stix")
	label.set_math_fontfamily("stixsans")
	label.set_math_fontfamily("custom")
	label.set_fontvariant("small-caps")
	label.set_fontvariant("normal")
	label.set_fontweight('normal')# weight : {a numeric value in range 0-1000, 'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'}
	label.set_fontsize(13)
