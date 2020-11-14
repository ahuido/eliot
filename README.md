## Naming specification.

Use database to store poems by poets.
每首诗一个条目，按照 id 进行区分。

根据几十首不同的诗作出一个范本，来设计数据库。

- poets
  - name
  - born
  - died
  
- poems

shakespeare
```
CREATE TABLE  _poet (
id     SMALLINT ,
given_name    VARCHAR(15),
middle_name   VARCHAR(15),
family_name   VARCHAR(15),
born   DATE,
died   DATE);
```

```
INSERT INTO _poet (id, given_name, family_name) VALUES (1, 'Walt', 'Whitman');
```

```

```
Wordsworth, William
Shakespeare, William
Blake, William
Kipling, Rudyard
Yeats, William Butler
Tennyson, Alfred Lord
Rossetti, Christina
Keats, John
Shelley, Percy Bysshe
Carroll, Lewis
Gibran, Kahlil
Whitman, Walt
Dickinson, Emily
Wilde, Oscar
Browning, Elizabeth Barrett
Pessoa, Fernando
Eliot, Thomas Stearns
Byron, George Gordon
Homer
Milton, John
Hardy, Thomas
Tagore, Robindranath
Pound, Ezra
Alighieri, Dante
Burns, Robert
Pushkin, Aleksandr
Frost, Robert
Donne, John
Emerson, Ralph Waldo
Lawrence, David Herbert
Chaucer, Geoffrey
Browning, Robert
Hopkins, Gerard Manley
Cmmings, Edward Estlin
.
├── alighieri, dante
│   └── The Divine Comedy of Dante by H. W. Longfellow .txt
├── blake, william
│   ├── Illustrations of The Book of Job.txt
│   ├── Mary Wollstonecraft's Original Stories.txt
│   ├── Poems of William Blake.txt
│   ├── Songs of Innocence and Songs of Experience.txt
│   └── The Marriage of Heaven and Hell.txt
├── browing, elizabeth barrett
│   ├── Aurora Leigh.txt
│   ├── 'He Giveth His Beloved Sleep'.txt
│   ├── O May I Join the Choir Invisible! and Other Favorite Poems.txt
│   ├── Sonnets from the Portuguese.txt
│   ├── The Poetical Works of Elizabeth Barrett Browning, Vol. I.txt
│   ├── The Poetical Works of Elizabeth Barrett Browning Volume II.txt
│   └── The Poetical Works of Elizabeth Barrett Browning, Volume IV.txt
├── browning, robert
│   ├── Browning's Shorter Poems.txt
│   ├── Christmas Eve.txt
│   ├── Dramatic Romances.txt
│   ├── Men and Women.txt
│   ├── Pomegranates from an English Garden.txt
│   ├── Selections from the Poems and Plays of Robert Browning .txt
│   └── The Complete Poetic and Dramatic Works of Robert Browning.txt
├── burns, robert
│   ├── Poems And Songs Of Robert Burns.txt
│   ├── Tam O'Shanter.txt
│   └── The Complete Works of Robert Burns- Containing his Poems, Songs, and Correspondence.txt
├── byron, george gordon
│   ├── Byron's Poetical Works, Vol. 1.txt
│   ├── Childe Harold's Pilgrimage.txt
│   ├── Don Juan.txt
│   ├── Fugitive Pieces.txt
│   ├── The Works of Lord Byron Poetry, Volume V..txt
│   ├── The Works Of Lord Byron, Vol. 3.txt
│   ├── The Works of Lord Byron, Vol. 7. Poetry.txt
│   ├── The Works of Lord Byron, Volume 2 .txt
│   ├── The Works of Lord Byron, Volume 4.txt
│   └── The Works of Lord Byron, Volume 6.txt
├── carroll, lewis
│   ├── Phantasmagoria and Other Poems.txt
│   ├── Rhyme? And Reason?.txt
│   ├── Songs From Alice in Wonderland and Through the Looking-Glass.txt
│   └── Three Sunsets and Other Poems.txt
├── chaucer, geoffrey
│   ├── Chaucer's Works, Volume 1.txt
│   ├── Chaucer's Works, Volume 2.txt
│   ├── Chaucer's Works, Volume 3.txt
│   ├── Chaucer's Works, Volume 4.txt
│   ├── Chaucer's Works, Volume 5.txt
│   ├── Chaucer's Works, Volume 6.txt
│   ├── The Canterbury Tales and Other Poems.txt
│   └── Troilus and Criseyde.txt
├── cummings, edward estlin
│   └── Eight Harvard Poets.txt
├── dickinson, emily
│   ├── Poems [Series 1] .txt
│   ├── Poems [Series 2].txt
│   ├── Poems- Third Series.txt
│   └── Poems- Three Series, Complete.txt
├── donne, john
│   ├── The Poems of John Donne [2 vols.] Volume I.txt
│   └── The Poems of John Donne, Volume II (of 2).txt
├── eliot, thomas stearns
│   ├── Poems.txt
│   ├── Prufrock and Other Observations.txt
│   └── The Waste Land.txt
├── emerson, ralph waldo
│   └── Poems.txt
├── frost, robert
│   ├── A Boy's Will.txt
│   ├── American Poetry, 1922 A Miscellany.txt
│   ├── Mountain Interval.txt
│   ├── New Hampshire, A Poem; with Notes and Grace Notes .txt
│   ├── North of Boston.txt
│   └── Selected Poems.txt
├── gibran, kahlil
│   ├── The Forerunner His Parables and Poems .txt
│   ├── The Madman .txt
│   ├── The Prophet.txt
│   └── Twenty Drawings.txt
├── hardy, thomas
│   ├── Late Lyrics and Earlier with many other verses.txt
│   ├── Moments of Vision and Miscellaneous Verses.txt
│   ├── Poems of the Past and the Present.txt
│   ├── Satires of Circumstance Lyrics and Reveries with Miscellaneous Pieces .txt
│   └── Time's Laughingstocks and Other Verses.txt
├── homer
│   ├── Iliad.txt
│   ├── The Iliad.txt
│   └── The Odyssey.txt
├── hopkins, gerard manley
│   └── Poems.txt
├── keats, john
│   ├── A Day with Keats.txt
│   ├── Endymion A Poetic Romance.txt
│   ├── Lamia.txt
│   ├── Poems 1817.txt
│   └── Poems Published in 1820.txt
├── kipling, rudyard
│   ├── A Song of the English.txt
│   ├── Songs from Books.txt
│   ├── The Five Nations, Volume II.txt
│   ├── The Five Nations, Volume I.txt
│   ├── The Seven Seas.txt
│   ├── The Years Between.txt
│   └── Verses 1889-1896.txt
├── lawrence, david herbert
│   ├── Amores Poems.txt
│   ├── Bay A Book of Poems.txt
│   ├── Birds, Beasts and Flowers.txt
│   ├── Georgian Poetry 1920-22.txt
│   ├── Look! We Have Come Through!.txt
│   ├── Love Poems and Others.txt
│   ├── New Poems.txt
│   └── Tortoises.txt
├── milton, john
│   ├── Milton's Comus.txt
│   ├── Minor Poems by Milton.txt
│   ├── Paradise Lost.txt
│   ├── Paradise Regained.txt
│   └── The Poetical Works of John Milton.txt
├── pessoa, fernando
│   ├── 35 Sonnets.txt
│   └── Antinous- A Poem.txt
├── pound, ezra
│   ├── Exultations.txt
│   ├── Hugh Selwyn Mauberley.txt
│   ├── Personae.txt
│   └── Poems 1918-21.txt
├── pushkin, aleksandr
│   └── Poems.txt
├── README.md
├── rossetti, christina
│   ├── Goblin Market, The Prince's Progress, and Other Poems.txt
│   └── Poems.txt
├── shakespeare, william
│   ├── Shakespeare's Sonnets.txt
│   └── The Complete Works of William Shakespeare.txt
├── shelley, percy bysshe
│   ├── A Defence of Poetry and Other Essays.txt
│   ├── Adonais.txt
│   ├── O May I Join the Choir Invisible! and Other Favorite Poems.txt
│   ├── Peter Bell the Third .txt
│   ├── The Complete Poetical Works of Percy Bysshe Shelley Volume III.txt
│   ├── #The Complete Poetical Works of Percy Bysshe Shelley Volume II.txt#
│   ├── The Complete Poetical Works of Percy Bysshe Shelley Volume II.txt
│   ├── The Complete Poetical Works of Percy Bysshe Shelley Volume I.txt
│   ├── The Daemon of the World.txt
│   └── The Witch of Atlas .txt
├── tagore, robindranath
│   ├── Fruit-Gathering.txt
│   ├── Gitanjali.txt
│   ├── Songs of Kabir.txt
│   ├── Stray Birds.txt
│   ├── The Crescent Moon.txt
│   ├── The Fugitive.txt
│   └── The Gardener.txt
├── tennyson, alfred lord
│   ├── A Day with the Poet Tennyson.txt
│   ├── Beauties of Tennyson.txt
│   ├── Enoch Arden, &c..txt
│   ├── Idylls of the King.txt
│   ├── Lady Clare.txt
│   ├── Maud, and Other Poems.txt
│   ├── Queen Mary and Harold.txt
│   ├── Selections from Wordsworth and Tennyson.txt
│   ├── The Early Poems of Alfred, Lord Tennyson.txt
│   ├── The Last Tournament.txt
│   ├── The Princess.txt
│   └── The Suppressed Poems of Alfred Lord Tennyson.txt
├── whitman, walt
│   ├── A Day with Walt Whitman.txt
│   ├── Complete Prose Works.txt
│   ├── Drum Taps.txt
│   ├── Leaves of Grass.txt
│   ├── Memories of Lincoln.txt
│   ├── Poems By Walt Whitman.txt
│   └── The Patriotic Poems of Walt Whitman.txt
├── wilde, oscar
│   ├── Charmides and Other Poems .txt
│   ├── Poems.txt
│   ├── Rose Leaf and Apple Leaf.txt
│   ├── Selected Poems of Oscar Wilde.txt
│   └── The Ballad of Reading Gaol.txt
├── wordsworth, william
│   ├── Lyrical Ballads 1798.txt
│   ├── Lyrical Ballads with Other Poems, 1800, Vol. 2.txt
│   ├── Lyrical Ballads, With Other Poems, 1800, Vol. I..txt
│   ├── Poems In Two Volumes, Vol. 1.txt
│   ├── Poems In Two Volumes, Vol. 2.txt
│   ├── Prefaces and Prologues to Famous Books with Introductions, Notes and Illustrations.txt
│   ├── Selections from Wordsworth and Tennyson.txt
│   ├── The Poetical Works of William Wordsworth, Vol. III.txt
│   ├── The Poetical Works of William Wordsworth, Vol. II. .txt
│   ├── The Poetical Works of William Wordsworth, Vol. I.txt
│   ├── The Poetical Works of William Wordsworth, Vol. IV.txt
│   ├── The Poetical Works of William Wordsworth, Vol. VIII.txt
│   ├── The Poetical Works of William Wordsworth, Vol. VII.txt
│   ├── The Poetical Works of William Wordsworth, Vol. VI.txt
│   ├── The Poetical Works of William Wordsworth, Vol. V.txt
│   └── The Prose Works of William Wordsworth For the First Time Collected, With Additions from Unpublished Manuscripts. In Three Volumes..txt
└── yeats, william butler
    ├── A Book of Irish Verse.txt
    ├── Poems.txt
    ├── Responsibilities and Other Poems .txt
    ├── The Collected Works in Verse and Prose of William Butler Yeats, Vol. 1.txt
    ├── The Collected Works in Verse and Prose of William Butler Yeats, Vol. 2.txt
    ├── The Collected Works in Verse and Prose of William Butler Yeats, Vol. 3.txt
    ├── The Collected Works in Verse and Prose of William Butler Yeats, Vol. 4.txt
    ├── The Collected Works in Verse and Prose of William Butler Yeats, Vol. 5.txt
    ├── The Collected Works in Verse and Prose of William Butler Yeats, Vol. 6.txt
    ├── The Collected Works in Verse and Prose of William Butler Yeats, Vol. 7.txt
    └── The Collected Works in Verse and Prose of William Butler Yeats, Vol. 8.txt

34 directories, 180 files
