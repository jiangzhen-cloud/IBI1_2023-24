import blosum as bl
SLC6A4_HUMAN="METTPLNSQKQLSACEDGEDCQENGVLQKVVPTPGDKVESGQISNGYSAVPSPGAGDDTRHSIPATTTTLVAELHQGERETWGKKVDFLLSVIGYAVDLGNVWRFPYICYQNGGGAFLLPYTIMAIFGGIPLFYMELALGQYHRNGCISIWRKICPIFKGIGYAICIIAFYIASYYNTIMAWALYYLISSFTDQLPWTSCKNSWNTGNCTNYFSEDNITWTLHSTSPAEEFYTRHVLQIHRSKGLQDLGGISWQLALCIMLIFTVIYFSIWKGVKTSGKVVWVTATFPYIILSVLLVRGATLPGAWRGVLFYLKPNWQKLLETGVWIDAAAQIFFSLGPGFGVLLAFASYNKFNNNCYQDALVTSVVNCMTSFVSGFVIFTVLGYMAEMRNEDVSEVAKDAGPSLLFITYAEAIANMPASTFFAIIFFLMLITLGLDSTFAGLEGVITAVLDEFPHVWAKRRERFVLAVVITCFFGSLVTLTFGGAYVVKLLEEYATGPAVLTVALIEAVAVSWFYGITQFCRDVKEMLGFSPGWFWRICWVAISPLFLLFIICSFLMSPPQLRLFQYNYPYWSIILGYCIGTSSFICIPTYIAYRLIITPGTFKERIIKSITPETPTEIPCGDIRLNAV"
SLC6A4_MOUSE="METTPLNSQKVLSECKDKEDCQENGVLQKGVPTPADKAGPGQISNGYSAVPSTSAGDEAPHSTPAATTTLVAEIHQGERETWGKKMDFLLSVIGYAVDLGNIWRFPYICYQNGGGAFLLPYTIMAIFGGIPLFYMELALGQYHRNGCISIWKKICPIFKGIGYAICIIAFYIASYYNTIIAWALYYLISSFTDQLPWTSCKNSWNTGNCTNYFAQDNITWTLHSTSPAEEFYLRHVLQIHQSKGLQDLGTISWQLALCIMLIFTIIYFSIWKGVKTSGKVVWVTATFPYIVLSVLLVRGATLPGAWRGVVFYLKPNWQKLLETGVWVDAAAQIFFSLGPGFGVLLAFASYNKFNNNCYQDALVTSVVNCMTSFVSGFVIFTVLGYMAEMRNEDVSEVAKDAGPSLLFITYAEAIANMPASTFFAIIFFLMLITLGLDSTFAGLEGVITAVLDEFPHIWAKRREWFVLIVVITCILGSLLTLTSGGAYVVTLLEEYATGPAVLTVALIEAVVVSWFYGITQFCSDVKEMLGFSPGWFWRICWVAISPLFLLFIICSFLMSPPQLRLFQYNYPHWSIILGYCIGTSSVICIPIYIIYRLISTPGTLKERIIKSITPETPTEIPCGDIRMNAV"
SLC6A4_RAT="METTPLNSQKVLSECKDREDCQENGVLQKGVPTTADRAEPSQISNGYSAVPSTSAGDEASHSIPAATTTLVAEIRQGERETWGKKMDFLLSVIGYAVDLGNIWRFPYICYQNGGGAFLLPYTIMAIFGGIPLFYMELALGQYHRNGCISIWRKICPIFKGIGYAICIIAFYIASYYNTIIAWALYYLISSLTDRLPWTSCTNSWNTGNCTNYFAQDNITWTLHSTSPAEEFYLRHVLQIHQSKGLQDLGTISWQLTLCIVLIFTVIYFSIWKGVKTSGKVVWVTATFPYIVLSVLLVRGATLPGAWRGVVFYLKPNWQKLLETGVWVDAAAQIFFSLGPGFGVLLAFASYNKFNNNCYQDALVTSVVNCMTSFVSGFVIFTVLGYMAEMRNEDVSEVAKDAGPSLLFITYAEAIANMPASTFFAIIFFLMLITLGLDSTFAGLEGVITAVLDEFPHIWAKRREWFVLIVVITCVLGSLLTLTSGGAYVVTLLEEYATGPAVLTVALIEAVAVSWFYGITQFCSDVKEMLGFSPGWFWRICWVAISPLFLLFIICSFLMSPPQLRLFQYNYPHWSIVLGYCIGMSSVICIPTYIIYRLISTPGTLKERIIKSITPETPTEIPCGDIRMNAV"
BLOSUM62=bl.BLOSUM(62)
def calculate_score(seq1, seq2, blosum62):
    score = 0
    for i in range(len(seq1)):
        score += blosum62[seq1[i]][seq2[i]]
    return score
def align_sequences(seq1, seq2, blosum62):
    score = calculate_score(seq1, seq2, blosum62)
    identical_count = sum(1 for a, b in zip(seq1, seq2)if a == b )
    identity_percentage = (identical_count / len(seq1)) * 100
    return score, identity_percentage

score1, identity_percentage1 = align_sequences(SLC6A4_HUMAN, SLC6A4_MOUSE, BLOSUM62)
print(f"Alignment score: {score1}")
print(f"Percentage of identical amino acids: {identity_percentage1}%")
score2, identity_percentage2 = align_sequences(SLC6A4_HUMAN, SLC6A4_RAT, BLOSUM62)
print(f"Alignment score: {score2}")
print(f"Percentage of identical amino acids: {identity_percentage2}%")
score3, identity_percentage3 = align_sequences(SLC6A4_MOUSE, SLC6A4_RAT, BLOSUM62)
print(f"Alignment score: {score3}")
print(f"Percentage of identical amino acids: {identity_percentage3}%")