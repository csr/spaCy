from __future__ import unicode_literals
import plac
import io

def main(in_loc, out_loc):
    this_key = None
    this_freq = 0
    df = 0
    with io.open(out_loc, 'w', encoding='utf8') as out_file:
        for line in io.open(in_loc, encoding='utf8'):
            line = line.strip()
            if not line:
                continue
            freq, key = line.split('\t', 1)
            freq = int(freq)
            if this_key is not None and key != this_key:
                out_file.write('%d\t%d\t%s\n' % (this_freq, df, this_key))
                this_key = key
                this_freq = freq
                df = 1
            else:
                this_freq += freq
                df += 1
                this_key = key
        out_file.write('%d\t%d\t%s\n' % (this_freq, df, this_key))


if __name__ == '__main__':
    plac.call(main)
