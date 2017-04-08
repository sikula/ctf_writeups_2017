For this challenge, we are given two image files: `A.png` and `B.png`.  If you open them in an image viewer, you will see a bunch of black and white "dots". Hmmm... what do these mean?

After a bit of research, I stumbled upon this wikipedia article: [Visual Cryptography](https://en.wikipedia.org/wiki/Visual_cryptography).

Alright, so lets just `XOR` the two images together.  My first thought was to use the `ImageMagik` library, but then I stumbled upon another image processing library, [gmic](https://github.com/dtschump/gmic), which is a bit easier to use.

Now, we just need to do it!
```bash
$ gmic A.png B.png -blend xor -o flag.png
```
