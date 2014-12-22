%{?_javapackages_macros:%_javapackages_macros}
Name:          boilerpipe
Version:       1.2.0
Release:       3.1
Summary:       Boilerplate Removal and Fulltext Extraction from HTML pages
Group:         Development/Java
License:       ASL 2.0
Url:           http://code.google.com/p/boilerpipe/
Source0:       http://boilerpipe.googlecode.com/files/%{name}-%{version}-src.tar.gz
Source1:       http://boilerpipe.googlecode.com/svn/repo/de/l3s/%{name}/%{name}/%{version}/%{name}-%{version}.pom
# use system libraries
Patch0:        %{name}-1.2.0-libdir-patch
# remove embedded nekohtml
Patch1:        %{name}-1.2.0-nekohtml-patch

BuildRequires: java-devel
BuildRequires: javapackages-tools

BuildRequires: ant
BuildRequires: nekohtml
BuildRequires: xerces-j2

Requires:      nekohtml

Requires:      java-headless
Requires:      javapackages-tools
BuildArch:     noarch

%description
The boilerpipe library provides algorithms to detect and
remove the surplus "clutter" (boilerplate, templates)
around the main textual content of a web page.

The library already provides specific strategies 
for common tasks (for example: news article extraction) and
may also be easily extended for individual problem settings.

Extracting content is very fast (milliseconds), just needs the
input document (no global or site-level information required) and
is usually quite accurate. 

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
find . -iname '*.jar' -delete
find . -iname '*.class' -delete

%patch0 -p0
cp %{SOURCE1} pom.xml
%patch1 -p1

# fix non ASCII chars
for s in src/main/de/l3s/boilerpipe/BoilerpipeInput.java \
 src/main/de/l3s/boilerpipe/BoilerpipeInput.java \
 src/main/de/l3s/boilerpipe/BoilerpipeFilter.java \
 src/main/de/l3s/boilerpipe/BoilerpipeExtractor.java \
 src/main/de/l3s/boilerpipe/BoilerpipeProcessingException.java \
 src/main/de/l3s/boilerpipe/conditions/TextBlockCondition.java \
 src/main/de/l3s/boilerpipe/document/TextBlock.java \
 src/main/de/l3s/boilerpipe/document/TextDocumentStatistics.java \
 src/main/de/l3s/boilerpipe/document/TextDocument.java \
 src/main/de/l3s/boilerpipe/estimators/SimpleEstimator.java \
 src/main/de/l3s/boilerpipe/extractors/LargestContentExtractor.java \
 src/main/de/l3s/boilerpipe/extractors/DefaultExtractor.java \
 src/main/de/l3s/boilerpipe/extractors/NumWordsRulesExtractor.java \
 src/main/de/l3s/boilerpipe/extractors/KeepEverythingWithMinKWordsExtractor.java \
 src/main/de/l3s/boilerpipe/extractors/ExtractorBase.java \
 src/main/de/l3s/boilerpipe/extractors/ArticleSentencesExtractor.java \
 src/main/de/l3s/boilerpipe/extractors/CommonExtractors.java \
 src/main/de/l3s/boilerpipe/extractors/CanolaExtractor.java \
 src/main/de/l3s/boilerpipe/extractors/ArticleExtractor.java \
 src/main/de/l3s/boilerpipe/extractors/KeepEverythingExtractor.java \
 src/main/de/l3s/boilerpipe/filters/english/HeuristicFilterBase.java \
 src/main/de/l3s/boilerpipe/filters/english/KeepLargestFulltextBlockFilter.java \
 src/main/de/l3s/boilerpipe/filters/english/TerminatingBlocksFinder.java \
 src/main/de/l3s/boilerpipe/filters/english/IgnoreBlocksAfterContentFilter.java \
 src/main/de/l3s/boilerpipe/filters/english/IgnoreBlocksAfterContentFromEndFilter.java \
 src/main/de/l3s/boilerpipe/filters/english/DensityRulesClassifier.java \
 src/main/de/l3s/boilerpipe/filters/english/MinFulltextWordsFilter.java \
 src/main/de/l3s/boilerpipe/filters/english/NumWordsRulesClassifier.java \
 src/main/de/l3s/boilerpipe/filters/heuristics/SimpleBlockFusionProcessor.java \
 src/main/de/l3s/boilerpipe/filters/heuristics/BlockProximityFusion.java \
 src/main/de/l3s/boilerpipe/filters/heuristics/KeepLargestBlockFilter.java \
 src/main/de/l3s/boilerpipe/filters/heuristics/DocumentTitleMatchClassifier.java \
 src/main/de/l3s/boilerpipe/filters/heuristics/LabelFusion.java \
 src/main/de/l3s/boilerpipe/filters/heuristics/AddPrecedingLabelsFilter.java \
 src/main/de/l3s/boilerpipe/filters/heuristics/ExpandTitleToContentFilter.java \
 src/main/de/l3s/boilerpipe/filters/heuristics/ContentFusion.java \
 src/main/de/l3s/boilerpipe/filters/simple/MinWordsFilter.java \
 src/main/de/l3s/boilerpipe/filters/simple/LabelToBoilerplateFilter.java \
 src/main/de/l3s/boilerpipe/filters/simple/LabelToContentFilter.java \
 src/main/de/l3s/boilerpipe/filters/simple/InvertedFilter.java \
 src/main/de/l3s/boilerpipe/filters/simple/InvertedFilter.java \
 src/main/de/l3s/boilerpipe/filters/simple/MinClauseWordsFilter.java \
 src/main/de/l3s/boilerpipe/filters/simple/BoilerplateBlockFilter.java \
 src/main/de/l3s/boilerpipe/filters/simple/SplitParagraphBlocksFilter.java \
 src/main/de/l3s/boilerpipe/filters/simple/MarkEverythingContentFilter.java \
 src/main/de/l3s/boilerpipe/labels/DefaultLabels.java \
 src/main/de/l3s/boilerpipe/labels/ConditionalLabelAction.java \
 src/main/de/l3s/boilerpipe/labels/LabelAction.java \
 src/main/de/l3s/boilerpipe/sax/BoilerpipeSAXInput.java \
 src/main/de/l3s/boilerpipe/sax/HTMLHighlighter.java \
 src/main/de/l3s/boilerpipe/sax/BoilerpipeHTMLContentHandler.java \
 src/main/de/l3s/boilerpipe/sax/BoilerpipeHTMLParser.java \
 src/main/de/l3s/boilerpipe/sax/TagActionMap.java \
 src/main/de/l3s/boilerpipe/sax/InputSourceable.java \
 src/main/de/l3s/boilerpipe/sax/HTMLDocument.java \
 src/main/de/l3s/boilerpipe/sax/CommonTagActions.java \
 src/main/de/l3s/boilerpipe/sax/DefaultTagActionMap.java \
 src/main/de/l3s/boilerpipe/sax/HTMLFetcher.java \
 src/main/de/l3s/boilerpipe/sax/TagAction.java \
 src/main/de/l3s/boilerpipe/sax/MarkupTagAction.java \
 src/main/de/l3s/boilerpipe/util/UnicodeTokenizer.java;do
  native2ascii -encoding UTF8 ${s} ${s}
done

%build

ant

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 dist/%{name}-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}.jar
install -m 644 dist/%{name}-demo-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}-demo.jar
  
mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp javadoc/*/* %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%{_javadir}/%{name}-demo.jar
%doc LICENSE.txt NOTICE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt NOTICE.txt

%changelog
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.2.0-2
- Use Requires: java-headless rebuild (#1067528)

* Mon Jan 21 2013 gil cattaneo <puntogil@libero.it> 1.2.0-1
- initial rpm
