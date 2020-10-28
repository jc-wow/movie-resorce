<template>
  <div class="allvideobook">
    <div class="cover">
      <div class="book">
        <label for="page-1" class="book__page book__page--1"> </label>

        <label for="page-2" class="book__page book__page--4">
          <div class="page__content">
            <h1 class="page__content-title">I</h1>
            <div class="page__content-blockquote">
              <span class="page__content-blockquote-reference"
                >Encyclopedia Galactica*</span
              >
            </div>
            <div class="page__number">3</div>
          </div>
        </label>

        <!-- Resets the page -->
        <input type="radio" name="page" id="page-1" />

        <!-- Goes to the second page -->
        <input type="radio" name="page" id="page-2" />
        <label class="book__page book__page--2">
          <div class="book__page-front">
            <div class="page__content">
              <h1 class="page__content-book-title">Foundation</h1>
              <h2 class="page__content-author">Isaac Asimov</h2>

              <p class="page__content-credits">
                Introduction by
                <span>Paul Krugman</span>
              </p>

              <p class="page__content-credits">
                Illustrations by
                <span>Alex Wells</span>
              </p>

              <div class="page__content-copyright">
                <p>The Folio Society</p>
                <p>London - MMXII</p>
              </div>
            </div>
          </div>
          <div class="book__page-back">
            <div class="page__content">
              <h1 class="page__content-title">Contents</h1>

              <div class="page__number">2</div>
            </div>
          </div>
        </label>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AllVideoBook",
};
</script>

<style scoped lang="scss">


* {
  box-sizing: border-box;
}

.allvideobook {
  background-color: var(--body-bg);
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.cover {
  width: calc(var(--baseline) * 60);
  height: calc(var(--baseline) * 42.6);
  box-shadow: 0 0 100px rgba(0, 0, 0, 0.3);

  .book {
    width: 100%;
    height: 100%;
    display: flex;
    perspective: 1200px;

    &__page {
      position: relative;
      width: 50%;
      height: 100%;
      display: grid;
      transform: rotateY(0deg);
      transition: transform 0.9s cubic-bezier(0.645, 0.045, 0.355, 1);
      transform-origin: 0% 0%;
      background-color: var(--page-bg);
      background-image: linear-gradient(
        90deg,
        rgba(227, 227, 227, 1) 0%,
        rgba(247, 247, 247, 0) 18%
      );

      &:nth-of-type(1) {
        background-image: linear-gradient(
          -90deg,
          rgba(227, 227, 227, 1) 0%,
          rgba(247, 247, 247, 0) 18%
        );
      }

      &--1 {
        cursor: pointer;
        overflow: hidden;

        img {
          width: 100%;
          max-width: 100%;
          height: auto;
        }
      }

      &--2 {
        position: absolute;
        right: 0;
        pointer-events: none;
        transform-style: preserve-3d;
        background-color: var(--page-bg);
        background-image: linear-gradient(
          90deg,
          rgba(227, 227, 227, 1) 0%,
          rgba(247, 247, 247, 0) 18%
        );
      }

      &--4 {
        cursor: pointer;
        padding: 0 calc(var(--baseline) * 3);
      }

      &-front {
        position: absolute;
        width: 100%;
        height: 100%;
        transform: rotateY(0deg) translateZ(1px);
      }

      &-back {
        position: absolute;
        width: 100%;
        height: 100%;
        padding: 0 calc(var(--baseline) * 1.8);
        transform: rotateY(180deg) translateZ(1px);
      }

      .page__content {
        padding: var(--baseline);
        height: 100%;
        position: relative;
        text-align: center;

        &-book-title {
          font-family: var(--book-title);
          font-size: calc(var(--base-size) * 3);
          font-weight: bold;
          text-transform: uppercase;
          letter-spacing: 3px;
          color: var(--dark-text);
          margin-top: calc(var(--baseline) * 5);
          margin-bottom: calc(var(--baseline) * 2);
        }

        &-author {
          font-family: var(--title);
          font-size: calc(var(--base-size) * 1.2);
          font-weight: 100;
          text-transform: uppercase;
          color: var(--dark-text);
          border-top: 1px solid var(--dark-text);
          border-bottom: 1px solid var(--dark-text);
          display: inline-block;
          padding: calc(var(--baseline) / 2) calc(var(--baseline) / 5);
          margin-bottom: calc(var(--baseline) * 6);
        }

        &-credits {
          font-family: var(--title);
          text-transform: uppercase;
          font-size: calc(var(--base-size) * 0.8);
          margin-bottom: calc(var(--baseline) * 2);
          letter-spacing: 1px;

          span {
            display: block;
            font-size: calc(var(--base-size) * 1.2);
            letter-spacing: 0;
          }
        }

        &-copyright {
          position: absolute;
          width: calc(100% - (var(--baseline) * 2));
          bottom: calc(var(--baseline) * 2);
          font-family: var(--title);
          font-size: calc(var(--base-size) * 0.8);
          text-transform: uppercase;
        }

        &-title {
          font-family: var(--title);
          font-size: calc(var(--base-size) * 1);
          text-transform: uppercase;
          letter-spacing: 1px;
          margin-top: calc(var(--baseline) * 5);
          margin-bottom: calc(var(--baseline) * 3);
        }

        &-table {
          width: 100%;
          margin-top: calc(var(--baseline) * 2);

          td {
            font-family: var(--title);
            font-size: calc(var(--base-size) * 1);
            padding-bottom: calc(var(--baseline) * 1.5);
            text-transform: uppercase;
          }
        }

        &-blockquote {
          margin-bottom: calc(var(--baseline) * 2);
        }

        &-blockquote-text {
          font-family: var(--title);
          font-size: calc(var(--base-size) * 0.67);
          font-style: italic;
          text-align: justify;
        }

        &-blockquote-reference {
          font-family: var(--title);
          font-size: calc(var(--base-size) * 0.7);
          margin-top: calc(var(--baseline) * 0.3);
          float: right;
          text-transform: uppercase;
        }

        &-text {
          font-family: var(--title);
          font-size: calc(var(--base-size) * 0.67);
          text-align: justify;
          text-indent: var(--baseline);
        }
      }
      .page__number {
        position: absolute;
        bottom: var(--baseline);
        width: calc(100% - (var(--baseline) * 2));
        font-family: var(--title);
        font-size: calc(var(--base-size) * 0.67);
        text-align: center;
      }
    }

    input[type="radio"] {
      display: none;

      &:checked + .book__page {
        transition: transform 0.9s cubic-bezier(0.645, 0.045, 0.355, 1);
        transform: rotateY(-180deg);
      }
    }
  }
}
</style>