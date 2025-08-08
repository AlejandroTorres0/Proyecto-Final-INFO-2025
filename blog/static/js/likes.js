function toggleLike(a) {
      const img = a.querySelector('img');
      var valor_path = img.getAttribute('src');
      const vacioSrc = img.getAttribute('cora-vacio');
      const llenoSrc = img.getAttribute('cora-lleno');
      const deslikear = a.getAttribute('deslike');
      const likear = a.getAttribute('like');
      
        if (valor_path == vacioSrc) {
          img.src = llenoSrc;
          a.href = likear;
        } else {
          img.src = vacioSrc;
          a.href = deslikear;
        }
    }