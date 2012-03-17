function ipd = assign(ipd,y,varargin)
% IPDOUBLE/ASSIGN Assign an entire in-place double.
%
% assign(ipd,y) overwrites the contents of ipd with y.  The size of ipd and
% y must match.
%
% Example:
%    ipd = ipdouble(ones(5,1));
%    assign(ipd,pi*ones(5,1));

if (isempty(x))

    if any(size(size(ipd)) ~= size(size(y))) || ...
       any(size(ipd) ~= size(y))
        error('ipdouble:invalidParameter','In assign(ipd,y) size(ipd) must equal size(y).');
    end;

    %ipd(:) = y(:);
    %ipd(1) = 5;
    subs = {':'};
    S = struct('type','()','subs',[]);
    S.subs = subs;
    subsasgn(ipd,S,y);
else
    S = struct('type','()','subs',[]);
    S.subs = varargin;
    subsasgn(ipd,S,y);
end;