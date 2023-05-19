import FilterHeader from "./FilterHeader";
import Keyword from "./Keyword";

const AddFilter = () => {
  return (
    <div className="container max-w-[395px] mx-auto flex flex-col items-center justify-center">
      <FilterHeader />
      <form className="w-[390px] ml-[70px] mt-[32px] flex flex-col items-start justify-center">
        <label
          for="filtername"
          className="flex items-start font-bold text-gray-700 font-main"
        >
          필터 이름
        </label>
        <input
          type="text"
          id="filtername"
          className="mt-[8px] rounded-lg border-transparent flex-1 appearance-none border border-gray-300 w-[320px] py-2 px-4 bg-white text-gray-700 placeholder-gray-400 shadow-sm text-base focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent"
          name="filtername"
          placeholder=""
        />
        <p className="space-x-1 mt-[32px] font-main text-[16px] text-black font-bold">
          직무 키워드
        </p>
        <Keyword />
        <label
          for="location"
          className="mt-[32px] flex items-start font-bold text-gray-700 font-main"
        >
          회사 위치
        </label>
        <input
          type="text"
          id="location"
          className="mt-[5px] rounded-lg border-transparent flex-1 appearance-none border border-gray-300 w-[320px] py-2 px-4 bg-white text-gray-700 placeholder-gray-400 shadow-sm text-base focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent"
          name="location"
          placeholder=""
        />
        <label
          for="location"
          className="mt-[32px] flex items-start font-bold text-gray-700 font-main"
        >
          가져올 사이트
        </label>
      </form>
    </div>
  );
};

export default AddFilter;