from music21 import note, stream

N1 = note.Note('A6')
N1.duration.quarterLength = 2
N2 = note.Note('C6')
N2.duration.quarterLength = 0.3
N3 = note.Note('C6')
N3.duration.quarterLength = 0.3
N4 = note.Note('E6')
N4.duration.quarterLength = 0.3
N5 = note.Note('D6')
N5.duration.quarterLength = 0.6
N6 = note.Note('A6')
N6.duration.quarterLength = 0.6
N7 = note.Note('D6')
N7.duration.quarterLength = 0.3

N8 = note.Note('A6')
N8.duration.quarterLength = 2
N9 = note.Note('A6')
N9.duration.quarterLength = 0.3
N10 = note.Note('C6')
N10.duration.quarterLength = 0.3
N11 = note.Note('C6')
N11.duration.quarterLength = 0.3
N12 = note.Note('D6')
N12.duration.quarterLength = 0.6
N13 = note.Note('C6')
N13.duration.quarterLength = 0.6
N14 = note.Note('A6')
N14.duration.quarterLength = 0.3

N15 = note.Note('F6')
N15.duration.quarterLength = 2
N16 = note.Note('F6')
N16.duration.quarterLength = 0.3
N17 = note.Note('A6')
N17.duration.quarterLength = 0.3
N18 = note.Note('C6')
N18.duration.quarterLength = 0.3
N19 = note.Note('E6')
N19.duration.quarterLength = 0.6
N20 = note.Note('A6')
N20.duration.quarterLength = 0.6
N21 = note.Note('C6')
N21.duration.quarterLength = 0.3

Secuencia1 = [N1, N2, N3, N4, N5, N6, N7, N8, N9, N10, N11, N12, N13, N14, N15, N16, N17, N18, N19, N20, N21]
st = stream.Stream(Secuencia1)

st.write('midi', fp = "snakeMusic2.mid")