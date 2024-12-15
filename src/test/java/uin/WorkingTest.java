package uin;

import static org.assertj.core.api.Assertions.*;

import org.junit.jupiter.api.Test;

import java.util.Comparator;
import java.util.List;

class WorkingTest {

    @Test
    void createAListsTest() {
        List<List<String>> aListsTest = Working.createAListsTest();
        assertThatList(aListsTest)
                .isNotNull()
                .hasSize(10)
                .allSatisfy(
                        sublist -> assertThat(sublist)
                                .hasSize(3)
                )
                .doesNotHaveDuplicates();
    }

    @Test
    void sortTest() {
        List<List<String>> dataBiodata = List.of(
                List.of("udin", "petani"),
                List.of("saiful", "guru"),
                List.of("amir", "pemancing"),
                List.of("budi", "dokter"),
                List.of("andika", "insinyur"),
                List.of("siti", "perawat"),
                List.of("rahma", "pengusaha"),
                List.of("ferdi", "programmer"),
                List.of("lisa", "desainer"),
                List.of("andi", "pengacara"),
                List.of("nina", "dosen"),
                List.of("yusuf", "sopir"),
                List.of("hadi", "koki"),
                List.of("rani", "penulis"),
                List.of("fitri", "jurnalis"),
                List.of("toni", "arsitek"),
                List.of("fajar", "tukang kayu"),
                List.of("dewi", "seniman"),
                List.of("agung", "musisi"),
                List.of("sari", "penjahit")
        );
        List<List<String>> sortedList = Working.sortTest(dataBiodata);
        assertThatList(sortedList)
                .hasSameSizeAs(dataBiodata)
                .isSortedAccordingTo(Comparator.comparing(item -> item.get(1)))
        ;
    }

    @Test
    void stackTest() {
        String[][] expectAndProvide = {
                {"jawa", "awaj"},
                {"sunda", "adnus"},
                {"bali", "ilab"},
                {"batak", "katab"},
                {"minang", "gnanim"},
                {"bugis", "sigub"},
                {"aceh", "heca"},
                {"madura", "arudam"},
                {"flores", "serolf"},
                {"sasak", "kasas"},
                {"dayak", "kayad"},
                {"toraja", "ajarot"},
                {"banten", "netnab"},
                {"banjar", "rajnab"},
                {"ternate", "etanret"},
                {"tidore", "erodit"},
                {"maluku", "ukulam"},
                {"papua", "aupap"},
                {"ambon", "nobma"},
                {"kupang", "gnapuk"}
        };
        for (String[] strings : expectAndProvide) {
            assertThat(Working.stackTest(strings[0]))
                    .isNotEmpty()
                    .hasSize(4)
                    .isEqualTo(strings[1]);
        }
    }

    @Test
    void queueTest() {
        List<Integer> waktuPelanggan = List.of(5, 3, 8, 2, 6);
        assertThatList(Working.queueTest(waktuPelanggan))
                .isNotEmpty()
                .hasSize(2)
                .isEqualTo(List.of(14, 10));

    }
}