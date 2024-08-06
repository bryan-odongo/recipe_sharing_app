import React from "react";
import Layout from "../components/Layout/Layout";

//sample recipespage
const RecipesPage = ({ recipes,title }) => {
  const buttons = [
    { text: 'Filter by', className: 'bg-yellow-500 w-[216px]', icon: 'ext_8-' },
    { text: 'Add your recipe', className: 'bg-orange-400 w-[225px]', icon: 'ext_8-' },
    { text: 'Cuisines', className: 'bg-yellow-500 w-[218px]', icon: 'ext_9-' },
    { text: 'Cooking tips& Tricks', className: 'bg-amber-500 w-[260px]', icon: 'ext_10-' },
    { text: 'Get a recipe', className: 'bg-lime-500 w-[237px]', icon: 'ext_11-' }
  ];

  return (
    <Layout>
    <>
      <section className="flex relative flex-col items-start px-20 pt-20 pb-2.5 w-full font-medium leading-none text-white max-w-[1264px] min-h-[355px] rounded-[36px] max-md:px-5 max-md:max-w-full">
      <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/fd6a79af305b395d5d865f685436386c8b5a7b49542460eaa15588e3ee2a5def?apiKey=58b317da616247a4b89e0aef017f4704&&apiKey=58b317da616247a4b89e0aef017f4704" alt="Background for trending recipe" className="object-cover absolute inset-0 size-full" />
      <div className="relative text-2xl text-orange-600">Trending now</div>
      <h1 className="relative mt-2 text-4xl font-bold leading-[51px] w-[446px] max-md:max-w-full">
        Mike's famous salad <br /> with cheese
      </h1>
      <p className="relative mt-5 text-xl">By John Mike</p>
      <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/3a600bcd454b26b650283e32f538c702479b05a07bea0be4cb34823822298fe3?apiKey=58b317da616247a4b89e0aef017f4704&&apiKey=58b317da616247a4b89e0aef017f4704" alt="" className="object-contain self-center mt-10 aspect-[2.59] w-[88px]" />
      <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/1b726bacabfbab46460da8ddcc3d1607f9c17759dc7bccf74cc1802356f271f4?apiKey=58b317da616247a4b89e0aef017f4704&&apiKey=58b317da616247a4b89e0aef017f4704" alt="" className="object-contain self-center mt-4 aspect-[6.99] w-[49px]" />
    </section>
    <div className="flex flex-wrap gap-5 items-start self-start mt-8 ml-3 w-full text-base font-semibold leading-none text-white min-h-[86px] max-md:max-w-full">
      {buttons.map((button, index) => (
        <button key={index} className={`flex overflow-hidden gap-5 px-11 py-8 rounded-xl ${button.className} max-md:px-5`}>
          <span>{button.text}</span>
          <img loading="lazy" src={`http://b.io/${button.icon}`} alt="" className="object-contain shrink-0 aspect-square w-[26px]" />
        </button>
      ))}
    </div>
    {/*
      <section className="mt-14 w-full max-w-[1264px] max-md:mt-10 max-md:max-w-full">
      <h2 className="self-start mt-16 text-4xl font-semibold leading-none text-black max-md:mt-10">{title}</h2>
      <div className="flex gap-5 max-md:flex-col">
        {recipes.map((recipe, index) => (
          <div key={index} className="flex flex-col w-3/12 max-md:ml-0 max-md:w-full">
            <RecipeCard {...recipe} />
          </div>
        ))}
      </div>
    </section>
    */}
    </>
    </Layout>
  );
};

export default RecipesPage;