let HOME_PAGE = "./index.html"
const LINKEDIN = "https://www.linkedin.com/in/gabriele-ghisleni-bb553a199/"
const PORTFOLIO = "https://gabrieleghisleni.github.io/GG-website/#/home"
const GITHUB = "https://github.com/GabrieleGhisleni"
const COLOR_HOME = 'black'
const EMAIL = "gabriele.ghisleni01@gmail.com"

const importing = () => {
    document.write(`
    <link rel="stylesheet" href="./css/style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
    integrity="sha512-SfTiTlX6kk+qitfevl/7LibUOeJWlt9rbyDn92a1DqWOw9vWG2MFoays0sgObmWazO5BQPiFucnnEAjpAB+/Sw=="
    crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css"
        integrity="sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn" crossorigin="anonymous">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/axios/0.25.0/axios.min.js"
        integrity="sha512-/Q6t3CASm04EliI1QyIDAA/nDo9R8FQ/BULoUFyN4n/BDdyIxeH7u++Z+eobdmr11gG5D/6nPFyDlnisDwhpYA=="
        crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js"
        integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
        crossorigin="anonymous"></script>`
    )
}

const navbar = (path) => {
    (!(path))? HOME_PAGE = "": null
    importing()
    document.write(`

    <nav class="navbar navbar-expand navbar-light sticky-top">
    <a class="navbar-brand" href="${HOME_PAGE}">Gabriele Ghisleni 220982</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav mr-auto">
            <li class="nav-item">
                <a class="nav-link" href="${HOME_PAGE}">
                    <i class="fa fa-home fa-2x" style='color:${HOME_PAGE}' aria-hidden="true"></i> </a>
            </li>
        </ul>
    </div>
    </nav>
    ${path? `    <nav aria-label="breadcrumb">
    <ol class="breadcrumb" id="path">
        <li class="breadcrumb-item"><a href="${HOME_PAGE}">Home</a></li>
        <li class="breadcrumb-item active" aria-current="page">${path}</li>
        </ol>
    </nav>`: "<span></span>"}`
    )
}




const footer = () => {
    document.write(`
    <div class="footer">
    <div class="row"></div>
      <div class="col-12 text-center">
        <ul class="list-unstyled list-inline social">
          <li class="list-inline-item"><a href="${GITHUB}"><i class="fa fa-github-square fa-2x"></i></a></li>
          <li class="list-inline-item"><a href="mailto:${EMAIL}"><i class="fa fa-envelope-square fa-2x"></i></a></li>
          <li class="list-inline-item"><a href="${LINKEDIN}"><i class="fa fa-linkedin-square fa-2x"></i></a></li>
          <li class="list-inline-item"><a href="${PORTFOLIO}"><i class="fa fa-briefcase fa-2x"></i></a></li>
          <li><a href="#"><span >@Gabriele Ghisleni</span></a></li>
        </ul>
      </div>
    </div>
  </div>
    `)
};